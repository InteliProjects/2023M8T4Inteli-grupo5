import pandas as pd
import pytest
from mcdata.ManipularTabela import TableManipulator

# Substitua 'your_module' pelo nome real do módulo ou script onde a classe está definida.

@pytest.fixture
def sample_dataframe():
    data = {
        'Name': ['John', 'Alice', 'Bob'],
        'Age': [28, 35, 40],
        'City': ['New York', 'Paris', 'London']
    }
    return pd.DataFrame(data)

def test_process_table_remove_duplicates(sample_dataframe):
    tm = TableManipulator(sample_dataframe.copy())
    result_df = tm.process_table(remove_duplicates=True)
    assert len(result_df) == len(sample_dataframe.drop_duplicates())

def test_process_table_null_value_replacement(sample_dataframe):
    tm = TableManipulator(sample_dataframe.copy())
    null_replacement_value = 'Unknown'
    result_df = tm.process_table(null_value_replacement=null_replacement_value)
    assert result_df.isna().sum().sum() == 0  # No NaN values should be present
    assert (result_df == null_replacement_value).any().any()

def test_process_table_column_mapping(sample_dataframe):
    tm = TableManipulator(sample_dataframe.copy())
    column_mapping = {'Name': 'Full_Name', 'Age': 'Years'}
    result_df = tm.process_table(column_mapping=column_mapping)
    assert all(column in result_df.columns for column in column_mapping.values())

def test_process_table_column_value_mapping(sample_dataframe):
    tm = TableManipulator(sample_dataframe.copy())
    column_value_mapping = {'City': {'New York': 'NY', 'Paris': 'FR', 'London': 'UK'}}
    result_df = tm.process_table(column_value_mapping=column_value_mapping)
    assert all(result_df['City'].isin(column_value_mapping['City'].values()))

def test_process_table_all_operations(sample_dataframe):
    tm = TableManipulator(sample_dataframe.copy())
    remove_duplicates = True
    null_replacement_value = 'Unknown'
    column_mapping = {'Name': 'Full_Name', 'Age': 'Years'}
    column_value_mapping = {'City': {'New York': 'NY', 'Paris': 'FR', 'London': 'UK'}}

    result_df = tm.process_table(
        remove_duplicates=remove_duplicates,
        null_value_replacement=null_replacement_value,
        column_mapping=column_mapping,
        column_value_mapping=column_value_mapping
    )

    assert len(result_df) == len(sample_dataframe.drop_duplicates())
    assert result_df.isna().sum().sum() == 0
    assert (result_df == null_replacement_value).any().any()
    assert all(column in result_df.columns for column in column_mapping.values())
    assert all(result_df['City'].isin(column_value_mapping['City'].values()))

# Execute os testes usando o comando pytest no terminal
