from pyspark.sql import SparkSession
from pyarrow import csv, parquet

def csv_to_parquet(csv_filepath, parquet_filepath, delimiter=','):
   spark = SparkSession.builder.getOrCreate()
   df = spark.read.csv(csv_filepath, sep=delimiter, header=True, inferSchema=True)
   df.write.parquet(parquet_filepath)


def rds_to_parquet(rds_filepath, parquet_filepath):
   table = csv.read_csv(rds_filepath)
   parquet.write_table(table, parquet_filepath)




   


