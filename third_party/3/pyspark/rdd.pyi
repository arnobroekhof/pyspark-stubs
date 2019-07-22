# Stubs for pyspark.rdd (Python 3.5)
#

from typing import overload
from typing import Any, Callable, Dict, Generic, Hashable, Iterable, Iterator, List, Optional, Tuple, Union, TypeVar

from numpy import int32, int64, float32, float64, ndarray  # type: ignore

from pyspark._typing import SupportsOrdering
import pyspark.context
from pyspark.serializers import Serializer
from pyspark.storagelevel import StorageLevel
from pyspark.statcounter import StatCounter
from pyspark.sql.dataframe import DataFrame
from pyspark.sql._typing import LiteralType, DecimalLiteral, DateTimeLiteral
from py4j.java_gateway import JavaObject  # type: ignore


T = TypeVar('T')
U = TypeVar('U')
K = TypeVar('K', bound=Hashable)
V = TypeVar('V')
V1 = TypeVar('V1')
V2 = TypeVar('V2')
V3 = TypeVar('V3')
O = TypeVar('O', bound=SupportsOrdering)
NumberOrArray = TypeVar('NumberOrArray', float, int, complex, int32, int64, float32, float64, ndarray)

def portable_hash(x: Hashable) -> int: ...

class PythonEvalType:
    NON_UDF: int = ...
    SQL_BATCHED_UDF: int = ...
    SQL_SCALAR_PANDAS_UDF: int = ...
    SQL_GROUPED_MAP_PANDAS_UDF: int = ...
    SQL_GROUPED_AGG_PANDAS_UDF: int = ...
    SQL_WINDOW_AGG_PANDAS_UDF: int = ...
    SQL_SCALAR_PANDAS_ITER_UDF: int = ...
    SQL_MAP_PANDAS_ITER_UDF: int = ...    

class BoundedFloat(float):
    def __new__(cls, mean: float, confidence: float, low: float, high: float): ...

class Partitioner:
    numPartitions = ...  # type: int
    partitionFunc = ...  # type: Callable[[Any], int]
    def __init__(self, numPartitions, partitionFunc) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __call__(self, k: Any) -> int: ...

class RDD(Generic[T]):
    is_cached = ...  # type: bool
    is_checkpointed = ...  # type: bool
    ctx = ...  # type: pyspark.context.SparkContext
    partitioner = ...  # type: Optional[Partitioner]
    def __init__(self, jrdd: JavaObject, ctx: pyspark.context.SparkContext, jrdd_deserializer: Serializer = ...) -> None: ...
    def id(self) -> int: ...
    def __getnewargs__(self) -> Any: ...
    @property
    def context(self) -> pyspark.context.SparkContext: ...
    def cache(self) -> RDD[T]: ...
    def persist(self, storageLevel: StorageLevel = ...) -> RDD[T]: ...
    def unpersist(self, blocking: bool = ...) -> RDD[T]: ...
    def checkpoint(self) -> None: ...
    def isCheckpointed(self) -> bool: ...
    def localCheckpoint(self) -> None: ...
    def isLocallyCheckpointed(self) -> bool: ...
    def getCheckpointFile(self) -> Optional[str]: ...
    def map(self, f: Callable[[T], U], preservesPartitioning: bool = ...) -> RDD[U]: ...
    def flatMap(self, f: Callable[[T], Iterable[U]], preservesPartitioning: bool = ...) -> RDD[U]: ...
    def mapPartitions(self, f: Callable[[Iterable[T]], Iterable[U]], preservesPartitioning: bool = ...) -> RDD[U]: ...
    def mapPartitionsWithIndex(self, f: Callable[[int, Iterable[T]], Iterable[U]], preservesPartitioning: bool = ...) -> RDD[U]: ...
    def mapPartitionsWithSplit(self, f: Callable[[int, Iterable[T]], Iterable[U]], preservesPartitioning: bool = ...) -> RDD[U]: ...
    def getNumPartitions(self) -> int: ...
    def filter(self, f: Callable[[T], bool]) -> RDD[T]: ...
    def distinct(self, numPartitions: Optional[int] = ...) -> RDD[T]: ...
    def sample(self, withReplacement: bool, fraction: float, seed: Optional[int] = ...) -> RDD[T]: ...
    def randomSplit(self, weights: List[Union[int, float]], seed: Optional[int] = ...) -> List[RDD[T]]: ...
    def takeSample(self, withReplacement: bool, num: int, seed: Optional[int] = ...) -> List[T]: ...
    def union(self, other: RDD[U]) -> RDD[Union[T, U]]: ...
    def intersection(self, other: RDD[T]) -> RDD[T]: ...
    def __add__(self, other: RDD[T]) -> RDD[T]: ...
    @overload
    def repartitionAndSortWithinPartitions(self: RDD[Tuple[O, V]], numPartitions: Optional[int] = ..., partitionFunc: Callable[[O], int] = ..., ascending: bool = ...) -> RDD[Tuple[O, V]]: ...
    @overload
    def repartitionAndSortWithinPartitions(self: RDD[Tuple[K, V]], numPartitions: Optional[int], partitionFunc: Callable[[K], int], ascending: bool, keyfunc: Callable[[K], O]) -> RDD[Tuple[K, V]]: ...
    @overload
    def repartitionAndSortWithinPartitions(self: RDD[Tuple[K, V]], numPartitions: Optional[int] = ..., partitionFunc: Callable[[K], int] = ..., ascending: bool = ..., *, keyfunc: Callable[[K], O]) -> RDD[Tuple[K, V]]: ...
    @overload
    def sortByKey(self: RDD[Tuple[O, V]], ascending: bool = ..., numPartitions: Optional[int] = ...) -> RDD[Tuple[K, V]]: ...
    @overload
    def sortByKey(self: RDD[Tuple[K, V]], ascending: bool, numPartitions: int, keyfunc: Callable[[K], O]) -> RDD[Tuple[K, V]]: ...
    @overload
    def sortByKey(self: RDD[Tuple[K, V]], ascending: bool = ..., numPartitions: Optional[int] = ..., *, keyfunc: Callable[[K], O]) -> RDD[Tuple[K, V]]: ...
    def sortBy(self: RDD[T], keyfunc: Callable[[T], O], ascending: bool = ..., numPartitions: Optional[int] = ...) -> RDD[T]: ...
    def glom(self) -> RDD[List[T]]: ...
    def cartesian(self, other: RDD[U]) -> RDD[Tuple[T, U]]: ...
    def groupBy(self, f: Callable[[T], K] , numPartitions: Optional[int] = ..., partitionFunc: Callable[[K], int] = ...) -> RDD[Tuple[K, Iterable[T]]]: ...
    def pipe(self, command: str, env: Optional[Dict[str, str]] = ..., checkCode: bool = ...) -> RDD[str]: ...
    def foreach(self, f: Callable[[T], None]) -> None: ...
    def foreachPartition(self, f: Callable[[Iterable[T]], None]) -> None: ...
    def collect(self) -> List[T]: ...
    def reduce(self, f: Callable[[T, T], T]) -> T: ...
    def treeReduce(self, f: Callable[[T, T], T], depth: int = ...) -> T: ...
    def fold(self, zeroValue: T, op: Callable[[T, T], T]) -> T: ...
    def aggregate(self, zeroValue: U, seqOp: Callable[[U, T], U], combOp: Callable[[U, U], U]) -> U: ...
    def treeAggregate(self, zeroValue: U, seqOp: Callable[[U, T], U], combOp: Callable[[U, U], U], depth: int = ...) -> U: ...
    @overload
    def max(self: RDD[O]) -> O: ...
    @overload
    def max(self, key: Callable[[T], O]) -> T: ...
    @overload
    def min(self: RDD[O]) -> O: ...
    @overload
    def min(self, key: Callable[[T], O]) -> T: ...
    def sum(self: RDD[NumberOrArray]) -> NumberOrArray: ...
    def count(self) -> int: ...
    def stats(self: RDD[NumberOrArray]) -> StatCounter: ...
    def histogram(self, buckets: List[T]) -> Tuple[List[T], List[int]]: ...
    def mean(self: RDD[NumberOrArray]) -> NumberOrArray: ...
    def variance(self: RDD[NumberOrArray]) -> NumberOrArray: ...
    def stdev(self: RDD[NumberOrArray]) -> NumberOrArray: ...
    def sampleStdev(self: RDD[NumberOrArray]) -> NumberOrArray: ...
    def sampleVariance(self: RDD[NumberOrArray]) -> NumberOrArray: ...
    def countByValue(self: RDD[K]) -> Dict[K, int]: ...
    @overload
    def top(self: RDD[O], num: int) -> List[O]: ...
    @overload
    def top(self: RDD[T], num: int, key: Callable[[T], O]) -> List[T]: ...
    @overload
    def takeOrdered(self: RDD[O], num: int) -> List[O]: ...
    @overload
    def takeOrdered(self: RDD[T], num: int, key: Callable[[T], O]) -> List[T]: ...
    def take(self, num: int) -> List[T]: ...
    def first(self) -> T: ...
    def isEmpty(self) -> bool: ...
    def saveAsNewAPIHadoopDataset(self: RDD[Tuple[K, V]], conf: Dict[str, str], keyConverter: Optional[str] = ..., valueConverter: Optional[str] = ...) -> None: ...
    def saveAsNewAPIHadoopFile(self: RDD[Tuple[K, V]], path: str, outputFormatClass: str, keyClass: Optional[str] = ..., valueClass: Optional[str] = ..., keyConverter: Optional[str] = ..., valueConverter: Optional[str] = ..., conf: Optional[Dict[str, str]] = ...) -> None: ...
    def saveAsHadoopDataset(self: RDD[Tuple[K, V]], conf: Dict[str, str], keyConverter: Optional[str] = ..., valueConverter: Optional[str] = ...) -> None: ...
    def saveAsHadoopFile(self: RDD[Tuple[K, V]], path: str, outputFormatClass: str, keyClass: Optional[str] = ..., valueClass: Optional[str] = ..., keyConverter: Optional[str] = ..., valueConverter: Optional[str] = ..., conf: Optional[str] = ..., compressionCodecClass: Optional[str] = ...) -> None: ...
    def saveAsSequenceFile(self: RDD[Tuple[K, V]], path: str, compressionCodecClass: Optional[str] = ...) -> None: ...
    def saveAsPickleFile(self, path: str, batchSize: int = ...) -> None: ...
    def saveAsTextFile(self, path: str, compressionCodecClass: Optional[str] = ...) -> None: ...
    def collectAsMap(self: RDD[Tuple[K, V]]) -> Dict[K, V]: ...
    def keys(self: RDD[Tuple[K, V]]) -> RDD[K]: ...
    def values(self: RDD[Tuple[K, V]]) -> RDD[V]: ...
    def reduceByKey(self: RDD[Tuple[K, V]], func: Callable[[V, V], V], numPartitions: Optional[int] = ..., partitionFunc: Callable[[K], int] = ...) -> RDD[Tuple[K, V]]: ...
    def reduceByKeyLocally(self: RDD[Tuple[K, V]], func: Callable[[V, V], V]) -> Dict[K, V]: ...
    def countByKey(self: RDD[Tuple[K, V]]) -> Dict[K, int]: ...
    def join(self: RDD[Tuple[K, V]], other: RDD[Tuple[K, U]], numPartitions: Optional[int] = ...) -> RDD[Tuple[K, Tuple[V, U]]]: ...
    def leftOuterJoin(self: RDD[Tuple[K, V]], other: RDD[Tuple[K, U]], numPartitions: Optional[int] = ...) -> RDD[Tuple[K, Tuple[V, Optional[U]]]]: ...
    def rightOuterJoin(self: RDD[Tuple[K, V]], other: RDD[Tuple[K, U]], numPartitions: Optional[int] = ...) -> RDD[Tuple[K, Tuple[Optional[V], U]]]: ...
    def fullOuterJoin(self: RDD[Tuple[K, V]], other: RDD[Tuple[K, U]], numPartitions: Optional[int] = ...) -> RDD[Tuple[K, Tuple[Optional[V], Optional[U]]]]: ...
    def partitionBy(self: RDD[Tuple[K, V]], numPartitions: int, partitionFunc: Callable[[K], int] = ...) -> RDD[Tuple[K, V]]: ...
    def combineByKey(self: RDD[Tuple[K, V]], createCombiner: Callable[[V], U], mergeValue: Callable[[U, V], U], mergeCombiners: Callable[[U, U], U], numPartitions: Optional[int] = ..., partitionFunc: Callable[[K], int] = ...) -> RDD[Tuple[K, U]]: ...
    def aggregateByKey(self: RDD[Tuple[K, V]], zeroValue: U, seqFunc: Callable[[U, V], U], combFunc: Callable[[U, U], U], numPartitions: Optional[int] = ..., partitionFunc: Callable[[K], int] = ...) -> RDD[Tuple[K, U]]: ...
    def foldByKey(self: RDD[Tuple[K, V]], zeroValue: V, func: Callable[[V, V], V], numPartitions: Optional[int] = ..., partitionFunc: Callable[[K], int] = ...) -> RDD[Tuple[K, V]]: ...
    def groupByKey(self: RDD[Tuple[K, V]], numPartitions: Optional[int] = ..., partitionFunc: Callable[[K], int] = ...) -> RDD[Tuple[K, Iterable[V]]]: ...
    def flatMapValues(self: RDD[Tuple[K, V]], f: Callable[[V], Iterable[U]]) -> RDD[Tuple[K, U]]: ...
    def mapValues(self: RDD[Tuple[K, V]], f: Callable[[V], U]) -> RDD[Tuple[K, U]]: ...
    @overload
    def groupWith(self: RDD[Tuple[K, V]], __o: RDD[Tuple[K, V1]]) -> RDD[Tuple[K, Tuple[List[V], List[V1]]]]: ...
    @overload
    def groupWith(self: RDD[Tuple[K, V]], __o1: RDD[Tuple[K, V1]], __o2: RDD[Tuple[K, V2]]) -> RDD[Tuple[K, Tuple[List[V], List[V1], List[V2]]]]: ...
    @overload
    def groupWith(self: RDD[Tuple[K, V]], other1: RDD[Tuple[K, V1]], other2: RDD[Tuple[K, V2]], other3: RDD[Tuple[K, V3]]) -> RDD[Tuple[K, Tuple[List[V], List[V1], List[V2], List[V3]]]]: ...
    def cogroup(self: RDD[Tuple[K, V]], other: RDD[Tuple[K, V1]], numPartitions: Optional[int] = ...) -> RDD[Tuple[K, Tuple[List[V], List[V1]]]]: ...
    def sampleByKey(self: RDD[Tuple[K, V]], withReplacement: bool, fractions: Dict[K, Union[float, int]], seed: Optional[int] = ...) -> RDD[Tuple[K, V]]: ...
    def subtractByKey(self: RDD[Tuple[K, V]], other: RDD[Tuple[K, U]], numPartitions: Optional[int] = ...) -> RDD[Tuple[K, V]]: ...
    def subtract(self: RDD[T], other: RDD[T], numPartitions: Optional[int] = ...) -> RDD[T]: ...
    def keyBy(self: RDD[T], f: Callable[[T], K]) -> RDD[Tuple[K, T]]: ...
    def repartition(self, numPartitions: int) -> RDD[T]: ...
    def coalesce(self, numPartitions: int, shuffle: bool = ...) -> RDD[T]: ...
    def zip(self, other: RDD[U]) -> RDD[Tuple[T, U]]: ...
    def zipWithIndex(self) -> RDD[Tuple[T, int]]: ...
    def zipWithUniqueId(self) -> RDD[Tuple[T, int]]: ...
    def name(self) -> str: ...
    def setName(self, name: str) -> RDD[T]: ...
    def toDebugString(self) -> bytes: ...
    def getStorageLevel(self) -> StorageLevel: ...
    def lookup(self: RDD[Tuple[K, V]], key: K) -> List[V]: ...
    def countApprox(self, timeout: int, confidence: float = ...) -> int: ...
    def sumApprox(self: RDD[Union[float, int]], timeout: int, confidence: float = ...) -> BoundedFloat: ...
    def meanApprox(self: RDD[Union[float, int]], timeout: int, confidence: float = ...) -> BoundedFloat: ...
    def countApproxDistinct(self, relativeSD: float = ...) -> int: ...
    def toLocalIterator(self) -> Iterator[T]: ...
    def barrier(self: RDD[T]) -> RDDBarrier[T]: ...
    def toDF(self: RDD[Union[Tuple, List]]) -> DataFrame: ...

class RDDBarrier(Generic[T]):
    rdd = ...  # type: RDD[T]
    def __init__(self, rdd: RDD[T]) -> None: ...
    def mapPartitions(self, f: Callable[[Iterable[T]], Iterable[U]], preservesPartitioning: bool = ...) -> RDD[U]: ...

class PipelinedRDD(RDD[U], Generic[T, U]):
    func = ...  # type: Callable[[T], U]
    preservesPartitioning = ...  # type: bool
    is_cached = ...  # type: bool
    is_checkpointed = ...  # type: bool
    ctx = ...  # type: pyspark.context.SparkContext
    prev = ...  # type: RDD[T]
    partitioner = ...  # type: Optional[Partitioner]
    is_barrier = ...  # type: bool
    def __init__(self, prev: RDD[T], func: Callable[[Iterable[T]], Iterable[U]], preservesPartitioning: bool = ..., isFromBarrier: bool = ...) -> None: ...
    def getNumPartitions(self) -> int: ...
    def id(self) -> int: ...
