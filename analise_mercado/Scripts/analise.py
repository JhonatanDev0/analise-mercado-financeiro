import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar dados financeiros
# Substitua este exemplo por código para carregar seus próprios dados
# Por exemplo, você pode carregar dados de um arquivo CSV ou de uma API financeira
def carregar_dados():
    # Exemplo de dados fictícios
    dados = {
        'Data': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'Preço': [100, 110, 105],
        'Volume': [10000, 12000, 11000]
    }
    df = pd.DataFrame(dados)
    df['Data'] = pd.to_datetime(df['Data'])
    return df

# Realizar análise de dados
def analisar_dados(df):
    # Exemplo: calcular média e desvio padrão dos preços
    media_preco = df['Preço'].mean()
    desvio_padrao_preco = df['Preço'].std()

    print("Média de Preço:", media_preco)
    print("Desvio Padrão de Preço:", desvio_padrao_preco)

    # Exemplo: visualização dos preços ao longo do tempo
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='Data', y='Preço', data=df)
    plt.title('Preço ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Preço')
    plt.show()

# Função principal
def main():
    # Carregar dados
    dados = carregar_dados()

    # Realizar análise de dados
    analisar_dados(dados)

if __name__ == "__main__":
    main()
