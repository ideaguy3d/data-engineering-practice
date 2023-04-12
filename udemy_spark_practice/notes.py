"""

            ~ SparkSession Methods ~
- .sql() https://spark.apache.org/docs/3.0.2/api/python/pyspark.sql.html#pyspark.sql.SparkSession.sql
- .table() https://spark.apache.org/docs/3.0.2/api/python/pyspark.sql.html#pyspark.sql.SparkSession.table
- .read() https://spark.apache.org/docs/3.0.2/api/python/pyspark.sql.html#pyspark.sql.SparkSession.read
- .range() https://spark.apache.org/docs/3.0.2/api/python/pyspark.sql.html#pyspark.sql.SparkSession.range
- .createDataFrame() https://spark.apache.org/docs/3.0.2/api/python/pyspark.sql.html#pyspark.sql.SparkSession.createDataFrame

            ~ Row Methods ~
- .asDict() https://spark.apache.org/docs/3.0.2/api/python/pyspark.sql.html#pyspark.sql.Row.asDict
- .index() https://spark.apache.org/docs/3.0.2/api/python/pyspark.sql.html#pyspark.sql.Row.index
- .count() https://spark.apache.org/docs/3.0.2/api/python/pyspark.sql.html#pyspark.sql.Row.count
- row.keys() https://spark.apache.org/docs/3.0.2/api/python/pyspark.sql.html#pyspark.sql.Row.keys
 -- row.key or row['key'] https://spark.apache.org/docs/3.0.2/api/python/pyspark.sql.html#pyspark.sql.Row.__getitem__
- key in rows https://spark.apache.org/docs/3.0.2/api/python/pyspark.sql.html#pyspark.sql.Row.__contains__

            ~ Commonly used methods and properties of RDD objects in PySpark ~
Methods:
- collect(): returns all the elements in the RDD to the driver program. It should be used with caution as it can lead to OutOfMemoryErrors if the RDD is too large.
- count(): returns the number of elements in the RDD.
- take(n): returns the first n elements of the RDD.
- filter(func): returns a new RDD containing only the elements that satisfy the given predicate function.
- map(func): applies a function to each element of the RDD and returns a new RDD containing the results.
- flatMap(func): applies a function to each element of the RDD and returns a new RDD containing the flattened results.
- reduce(func): aggregates the elements of the RDD using the given binary operator function.
- foreach(func): applies a function to each element of the RDD without returning any results.
- distinct()

Properties:
- id: returns a unique identifier for the RDD.
- name: returns the name of the RDD.
- partitions: returns a list of the partitions that make up the RDD.
- is_cached: returns True if the RDD is cached in memory or on disk, otherwise False.
- is_checkpointed: returns True if the RDD has been checkpointed, otherwise False.
- storage_level: returns the storage level of the RDD.
- dependencies: returns a list of the RDDs that the current RDD depends on.
- context: returns the SparkContext object associated with the RDD.

These are just some of the commonly used methods and properties of RDD objects in PySpark. For a complete list, you can refer to the official PySpark documentation.
"""
tech = ['torch', 'spark', 'linux', 'airflow']
tech.sort()
print('tech sorted:')
print(tech)
