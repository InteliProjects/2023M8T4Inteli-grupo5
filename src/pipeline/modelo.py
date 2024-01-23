import psycopg2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from scipy.stats import pearsonr
from sklearn.preprocessing import LabelEncoder
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, first
from pyspark.sql.functions import col
import findspark
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from scipy.stats import pearsonr
from sklearn.preprocessing import LabelEncoder
findspark.init()
def create_spark_session(app_name):
    spark = SparkSession.builder.appName(app_name).getOrCreate()
    return spark

#Conexão com o redshift
def connect_redshift(host, port, user, password, database):
    conn = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    cursor = conn.cursor()
    return conn, cursor

#Função para executar query no redshift
def run_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()
#Função para transformar query em dataframe pandas
def query_to_df(cursor, query):
    df = pd.DataFrame(run_query(cursor, query))
    df.columns = [desc[0] for desc in cursor.description]
    return df

def train_model(data):
    # Pré-processamento dos dados
    le = LabelEncoder()
    data['sigla_uf'] = le.fit_transform(data['sigla_uf'])

    # Criar features e target
    features = ['preco', 'idCategory', 'sigla_uf', 'taxa_selic', 'taxa_exp_inflacao', 'USD']
    target = 'quantidade'

    X = data[features]
    y = data[target]

    # Dividir dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Criar e treinar o modelo de ensemble (Random Forest)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Fazer previsões
    predictions = model.predict(X_test)

    # Avaliar o modelo
    mse_global = mean_squared_error(y_test, predictions)
    print(f'Mean Squared Error: {mse_global}')

    # Mean Absolute Error (MAE)
    mae = mean_absolute_error(y_test, predictions)
    print(f"Mean Absolute Error (MAE): {mae}")

    # Root Mean Squared Error (RMSE)
    rmse = mean_squared_error(y_test, predictions, squared=False)
    print(f"Root Mean Squared Error (RMSE): {rmse}")

    # R-squared (R²)
    r2 = r2_score(y_test, predictions)
    print(f"R-squared (R²): {r2}")

    # Pearson correlation coefficient
    pearson_corr, _ = pearsonr(y_test, predictions)
    print(f"Pearson Correlation Coefficient: {pearson_corr}")

#Função para plotar gráfico de feature importance do modelo e salvar a imagem
def plot_feature_importance(model, features):
    importances = model.feature_importances_
    indices = np.argsort(importances)

    plt.figure(figsize=(10, 5))
    plt.title('Feature Importances')
    plt.barh(range(len(indices)), importances[indices], color='b', align='center')
    plt.yticks(range(len(indices)), [features[i] for i in indices])
    plt.xlabel('Importance')
    plt.savefig('feature_importance.png')
    

#Execução do pipeline modelo
def run_modelo():
    # Conexão com o Redshift
    conn, cursor = connect_redshift(
        host='host',
        port='port',
        user='user',
        password='password',
        database='database'
    )

    # Query para obter os dados
    query = """
    SELECT cnpj_vendas_bacen_final.produto, cnpj_vendas_bacen_final.preco, cnpj_vendas_bacen_final.quantidade, cnpj_vendas_bacen_final.usd, cnpj_vendas_bacen_final.taxa_selic, cnpj_vendas_bacen_final.taxa_exp_inflacao, densidade_g05_real.densidade_populacional_habitantes_km2, densidade_g05_real.area_km2, densidade_g05_real.numer0_populacional
    FROM cnpj_vendas_bacen_final
    INNER JOIN densidade_g05_real ON cnpj_vendas_bacen_final.id_municipio = densidade_g05_real.code_muni;
    """
    # Transformar query em dataframe pandas
    data = query_to_df(cursor, query)

    # Treinar modelo
    train_model(data)

    # Plotar feature importance
    features = ['preco', 'idCategory', 'sigla_uf', 'taxa_selic', 'taxa_exp_inflacao', 'USD']
    plot_feature_importance(model, features)

    # Fechar conexão com o Redshift
    cursor.close()
    conn.close()

    print('Pipeline Modelo executado com sucesso!')

#Execução do pipeline modelo
if __name__ == "__main__":
    run_modelo()




