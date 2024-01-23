import os
import pytest
from pyspark.sql import SparkSession
from pyarrow import csv, parquet

from mcdata.transformar import csv_to_parquet, rds_to_parquet

# Substitua 'your_module' pelo nome real do módulo ou script onde as funções estão definidas.

@pytest.fixture(scope="session")
def spark_session():
    spark = SparkSession.builder.master("local[2]").appName("pytest").getOrCreate()
    yield spark
    spark.stop()

@pytest.fixture(scope="session")
def temp_dir():
    temp_dir = "temp_test_dir"
    yield temp_dir
    if os.path.exists(temp_dir):
        os.rmdir(temp_dir)

def test_csv_to_parquet(spark_session, temp_dir):
    # Criar um DataFrame de exemplo para testar a função csv_to_parquet
    data = [("John", 28), ("Alice", 35), ("Bob", 40)]
    columns = ["name", "age"]
    df = spark_session.createDataFrame(data, columns)

    # Salvar o DataFrame em um arquivo CSV temporário
    csv_filepath = os.path.join(temp_dir, "test_csv_file.csv")
    df.write.csv(csv_filepath, header=True, mode="overwrite")

    # Chamar a função csv_to_parquet para converter o CSV temporário para Parquet
    parquet_filepath = os.path.join(temp_dir, "test_parquet_file")
    csv_to_parquet(csv_filepath, parquet_filepath)

    # Verificar se o arquivo Parquet foi criado
    assert os.path.exists(parquet_filepath)

def test_rds_to_parquet(temp_dir):
    # Criar um arquivo CSV temporário para testar a função rds_to_parquet
    csv_filepath = os.path.join(temp_dir, "test_csv_file.csv")
    with open(csv_filepath, "w") as csv_file:
        csv_file.write("name,age\nJohn,28\nAlice,35\nBob,40")

    # Chamar a função rds_to_parquet para converter o CSV temporário para Parquet
    parquet_filepath = os.path.join(temp_dir, "test_parquet_file")
    rds_to_parquet(csv_filepath, parquet_filepath)

    # Verificar se o arquivo Parquet foi criado
    assert os.path.exists(parquet_filepath)

# Execute os testes usando o comando pytest no terminal


