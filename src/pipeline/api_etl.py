import pandas as pd
import requests
import json
import numpy as np 
import boto3
import os
from mcdata.s3 import S3Uploader
from mcdata.ManipularTabela import TableManipulator
from api_link import url

def get_data():
    params = {
        "code": "pZh3gmJW_87epswrWDuB7CvQle-KqjsVh2ZJUaifiXd4AzFuOEy98w==",
        "table": "sale",
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
    else:
        raise ValueError(f"Erro ao obter dados: {response.status_code}")

    df = pd.DataFrame(data)
    
    return df

def transform_data(df):
    df.rename(columns={'category': 'produto', 'value': 'preco', 'amount': 'quantidade', 'saleDate': 'data'},
              inplace=True)
    df['produto'] = df['produto'].apply(lambda x: x['name'] if isinstance(x, dict) and 'name' in x else x)
    df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%dT%H:%M:%S', errors='coerce').dt.date
    df.to_csv('data/vendas.csv', index=False)

def upload(aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token):
    upload_vendas = S3Uploader(aws_access_key_id, aws_secret_access_key, bucket_name, aws_session_token)
    upload_vendas.upload_file('data/vendas.csv', 'vendas.csv')
    os.remove('data/vendas.csv')

def run():
    df = get_data()
    transform_data(df)
    upload('aws_access_key_id', 'aws_secret_access_key', 'bucket_name', 'aws_session_token')
    print('ETL executado com sucesso!')

if __name__ == "__main__":
    run()
