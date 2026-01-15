import pandas as pd

def carregar_dados(caminho_arquivo):
    """
    Carrega o arquivo CSV e retorna um DataFrame.
    """
    df = pd.read_csv(caminho_arquivo)
    return df

def limpar_dados(df):
    """
    Realiza limpeza básica dos dados.
    - Remove valores nulos
    - Cria coluna de faturamento
    """
    df = df.dropna()
    df["faturamento"] = df["quantidade"] * df["valor_unitario"]
    return df
