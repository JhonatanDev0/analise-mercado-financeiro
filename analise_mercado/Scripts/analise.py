import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas_datareader import data as pdr
import yfinance as yf

# Configurações padrão do Seaborn para gráficos
sns.set_style("whitegrid")

# Título do aplicativo
st.title('Visualização de Dados da Bolsa de Valores')

# Entrada para o ticker da ação
ticker = st.text_input('Insira o Ticker da Ação (ex: AAPL)')

# DataFrame vazio para armazenar os dados
df = pd.DataFrame()

# Carregar dados da bolsa de valores
try:
    yf.pdr_override()  # Sobrescreve o método de busca do Yahoo Finance
    df = pdr.get_data_yahoo(ticker, start='2022-01-01', end='2022-12-31')
except Exception as e:
    st.error(f'Erro ao carregar dados: {e}')

# Verifica se o DataFrame não está vazio antes de continuar
if not df.empty:
    # Mostra os primeiros registros dos dados
    st.write(df.head())

    # Análise descritiva dos dados
    st.subheader('Análise Descritiva dos Dados')
    st.write(df.describe())

    # Gráfico de linha dos preços de fechamento com Seaborn
    st.subheader('Gráfico de Linha - Preços de Fechamento')
    fig, ax = plt.subplots()
    sns.lineplot(x=df.index, y=df['Close'], ax=ax)
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento')
    st.pyplot(fig)

    # Gráfico de barras do volume de negociação com Matplotlib
    st.subheader('Gráfico de Barras - Volume de Negociação')
    fig, ax = plt.subplots()
    ax.bar(df.index, df['Volume'], color='skyblue')
    plt.xlabel('Data')
    plt.ylabel('Volume de Negociação')
    st.pyplot(fig)
