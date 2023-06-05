import pandas as pd
import matplotlib.pyplot as mp

AUTORES = ['Pedro Santos Tokar', 'Paulo César Gomes Rodrigues']

def questao_1(caminho):
    df = pd.read_csv(caminho)
    return df.shape[0]

def questao_2(caminho):
    df = pd.read_csv(caminho)
    casos_por_municipio = df["ID_MUNICIP"].value_counts()
    return casos_por_municipio

def questao_3():
    pass

def questao_4():
    pass

def questao_5():
    pass

def questao_6():
    pass

def questao_7():
    pass

def questao_8():
    pass

def questao_9():
    pass

def questao_10():
    pass
