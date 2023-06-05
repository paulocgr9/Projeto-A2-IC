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
    df = pd.read_csv(caminho)
    dicionario =  df["CS_SEXO"].value_counts().to_dict()
    if " " in dicionario.keys():
        del dicionario[" "]
    if "I" in dicionario.keys():
        del dicionario["I"]
    return dicionario

def questao_4():
    pass

def questao_5(caminho):
    df = pd.read_csv(caminho)
    estados_com_sigla = df["SG_UF_NOT"].replace(
        {"12":"AC", "27":"AL", "16":"AP", "13":"AM", "29": "BA", "23":"CE", "53":"DF", 
        "32":"ES", "52":"GO", "21":"MA", "51":"MT", "50":"MS", "31":"MG", "15":"PA",
        "25":"PB", "41":"PR", "26":"PE", "22":"PI", "24":"RN", "43":"RS", "33":"RJ", 
        "11":"RO", "14":"RR", "42":"SC", "35":"SP", "28":"SE", "17":"TO"}
    ).to_dict()
    return estados_com_sigla

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
