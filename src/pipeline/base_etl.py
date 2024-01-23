import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, LongType, IntegerType
import findspark
import os
from mcdata.s3 import S3Uploader
from mcdata.ManipularTabela import TableManipulator
from mcdata.dicionarios import uf

findspark.init()

def create_spark_session(app_name):
    spark = SparkSession.builder.appName(app_name).getOrCreate()
    return spark

def read_csv_to_spark(spark, file_path, header=True, delimiter=";"):
    return spark.read.option("header", header).option("delimiter", delimiter).csv(file_path)

def write_spark_to_parquet(spark_df, file_path):
    spark_df.write.mode("overwrite").parquet(file_path)

def remove_duplicates(spark_df):
    return spark_df.distinct()

def fillna_with_value(spark_df, column, value):
    return spark_df.fillna(value, subset=[column])

def dropna(spark_df):
    return spark_df.dropna()

def upload_file_to_s3(aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token, local_file_path, s3_file_path):
    uploader = S3Uploader(aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token)
    uploader.upload_file(local_file_path, s3_file_path)
    os.remove(local_file_path)

def run_cnpj_etl(spark, file_path, aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token):
    # Lê CSV para Spark DataFrame
    custom_schema = StructType([
    StructField("data", StringType(), True),
    StructField("cnpj", LongType(), False),
    StructField("cnpj_basico", IntegerType(), True),
    StructField("cnpj_ordem", IntegerType(), True),
    StructField("cnpj_dv", IntegerType(), True),
    StructField("identificador_matriz_filial", IntegerType(), True),
    StructField("nome_fantasia", StringType(), True),
    StructField("situacao_cadastral", IntegerType(), True),
    StructField("data_situacao_cadastral", StringType(), True),
    StructField("motivo_situacao_cadastral", IntegerType(), True),
    StructField("nome_cidade_exterior", StringType(), True),
    StructField("id_pais", IntegerType(), True),
    StructField("data_inicio_atividade", StringType(), True),
    StructField("cnae_fiscal_principal", IntegerType(), True),
    StructField("cnae_fiscal_secundaria", StringType(), True),
    StructField("sigla_uf", StringType(), True),
    StructField("id_municipio", IntegerType(), True),
    StructField("id_municipio_rf", IntegerType(), True),
    StructField("tipo_logradouro", StringType(), True),
    StructField("logradouro", StringType(), True),
    StructField("numero", StringType(), True),
    StructField("complemento", StringType(), True),
    StructField("bairro", StringType(), True),
    StructField("cep", StringType(), True),
    StructField("ddd_1", IntegerType(), True),
    StructField("telefone_1", StringType(), True),
    StructField("ddd_2", IntegerType(), True),
    StructField("telefone_2", IntegerType(), True),
    StructField("ddd_fax", IntegerType(), True),
    StructField("fax", StringType(), True),
    StructField("email", StringType(), True),
    StructField("situacao_especial", StringType(), True),
    StructField("data_situacao_especial", StringType(), True)
    ])
    cnpj_df = read_csv_to_spark(spark, file_path, header=True, delimiter=";", schema=custom_schema)

    # Transformações
    cnpj_df = remove_duplicates(cnpj_df)
    cnpj_df = fillna_with_value(cnpj_df, "nome_fantasia", "NAO INFORMADO")
    cnpj_df = dropna(cnpj_df)

    # Transformando em parquet
    write_spark_to_parquet(cnpj_df, "data/cnpj.parquet")

    # Upload para o S3
    upload_file_to_s3(aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token, "data/cnpj.parquet", "cnpj.parquet")

    print("ETL CNPJ executed successfully!")

def run_pof_etl(file_path, aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token):
    # Lendo CSV para Pandas DataFrame
    pof_df = pd.read_csv(file_path, sep=";")

    # Transformações
    pof_process = TableManipulator(pof_df)
    pof_process.process_table(remove_duplicates=True, null_value_replacement='NAO INFORMADO', column_value_mapping={'UF': uf()})

    # Convertendo para Spark DataFrame
    spark = create_spark_session("pipeline")
    pof_spark_df = spark.createDataFrame(pof_process)

    # Escrevendo para Parquet
    write_spark_to_parquet(pof_spark_df, "data/pof.parquet")

    # Upload para o S3
    upload_file_to_s3(aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token, "data/pof.parquet", "pof.parquet")

    print("ETL POF executed successfully!")

def run_bacen_etl(file_path, aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token):
    # lendo CSV para Pandas DataFrame
    bacen_df = pd.read_csv(file_path, sep=";")

    # Transformações
    bacen_df.fillna(0, inplace=True)

    # Convertendo para Spark DataFrame
    spark = create_spark_session("pipeline")
    bacen_spark_df = spark.createDataFrame(bacen_df)

    # Escrevendo para Parquet
    write_spark_to_parquet(bacen_spark_df, "data/bacen.parquet")

    # Upload para o S3
    upload_file_to_s3(aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token, "data/bacen.parquet", "bacen.parquet")

    print("ETL BACEN executed successfully!")

def run_ibge_densidade_etl(file_path, aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token):
    # lendo CSV para Spark DataFrame
    densidade_df = read_csv_to_spark(spark, file_path, header=True, inferSchema=True)

    # Transformações
    densidade_df = densidade_df.withColumnRenamed("NUMERO POPULACIONAL".strip(), "NUMERO_POPULACIONAL")

    # Escrevendo para Parquet
    write_spark_to_parquet(densidade_df, "data/densidade.parquet")

    # Upload para o S3
    upload_file_to_s3(aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token, "data/densidade.parquet", "densidade.parquet")

    print("ETL DENSIDADE + IBGE executed successfully!")

def run_anvisa_etl(file_path, aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token):
    # lendo CSV para Pandas DataFrame
    anvisa_df = pd.read_csv(file_path, sep=";")

    # Transformações
    anvisa_df.fillna(0, inplace=True)

    # Convertendo para Spark DataFrame
    spark = create_spark_session("pipeline")
    anvisa_spark_df = spark.createDataFrame(anvisa_df)

    # Escrevendo para Parquet
    write_spark_to_parquet(anvisa_spark_df, "data/anvisa.parquet")

    # Upload para o S3
    upload_file_to_s3(aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token, "data/anvisa.parquet", "anvisa.parquet")

    print("ETL ANVISA executed successfully!")

if __name__ == "__main__":
    spark = create_spark_session("pipeline")
    run_cnpj_etl(spark, "data/cnpj.csv", "aws_access_key_id", "aws_secret_access_key", "bucket_name", "aws_session_token")
    run_pof_etl("data/pof.csv", "aws_access_key_id", "aws_secret_access_key", "bucket_name", "aws_session_token")
    run_bacen_etl("data/bacen.csv", "aws_access_key_id", "aws_secret_access_key", "bucket_name", "aws_session_token")
    run_ibge_densidade_etl("data/densidade.csv", "aws_access_key_id", "aws_secret_access_key", "bucket_name", "aws_session_token")
    run_anvisa_etl("data/anvisa.csv", "aws_access_key_id", "aws_secret_access_key", "bucket_name", "aws_session_token")
