import pandas as pd
from pysus.preprocessing.decoders import decodifica_idade_SINAN

AUTORES = ['Pedro Santos Tokar', 'Paulo César Gomes Rodrigues']

dicionario_estados = {
    12:"AC", 27:"AL", 16:"AP", 13:"AM", 29:"BA", 23:"CE", 53:"DF", 32:"ES",
    52:"GO", 21:"MA", 51:"MT", 50:"MS", 31:"MG", 15:"PA", 25:"PB", 41:"PR",
    26:"PE", 22:"PI", 24:"RN", 43:"RS", 33:"RJ", 11:"RO", 14:"RR", 42:"SC",
    35:"SP", 28:"SE", 17:"TO"
}

def questao_1(caminho = "chagas2018.csv"):
    df = pd.read_csv(caminho)
    return df.shape[0]

def questao_2(caminho = "chagas2018.csv"):
    df = pd.read_csv(caminho)
    casos_por_municipio = df["ID_MUNICIP"].value_counts()
    return casos_por_municipio

def questao_3(caminho = "chagas2018.csv"):
    df = pd.read_csv(caminho)
    dicionario =  df["CS_SEXO"].value_counts().to_dict()
    if " " in dicionario.keys():
        del dicionario[" "]
    if "I" in dicionario.keys():
        del dicionario["I"]
    if not ("M" in dicionario.keys()):
        dicionario["M"] = 0
    if not ("F" in dicionario.keys()):
        dicionario["F"] = 0
    if dicionario["M"] > dicionario["F"]:
        return "M", dicionario
    elif dicionario["F"] > dicionario["M"]:
        return "F", dicionario
    else:
        return "F", dicionario

def questao_4(caminho = "chagas2018.csv"):
    df = pd.read_csv(caminho)
    df["IDADE_DECODIFICADA"] = decodifica_idade_SINAN(df.NU_IDADE_N, "Y")
    media = df["IDADE_DECODIFICADA"].mean()
    return media

def questao_5(caminho = "chagas2018.csv"):
    df = pd.read_csv(caminho)
    estados_com_sigla = df["SG_UF_NOT"].replace(dicionario_estados)
    contagem_por_estado = estados_com_sigla.value_counts().to_dict()
    for estado in dicionario_estados.values():
        if estado not in contagem_por_estado.keys():
            contagem_por_estado[estado] = 0
    return contagem_por_estado

def questao_6(caminho = "chagas2018.csv"):
    df = pd.read_csv(caminho)
    df["SG_UF_NOT"] = df["SG_UF_NOT"].replace(dicionario_estados)
    somente_homens = df[df["CS_SEXO"] == "M"]
    quant_por_estado = somente_homens["SG_UF_NOT"].value_counts().to_dict()
    for estado in dicionario_estados.values():
        if estado not in quant_por_estado.keys():
            quant_por_estado[estado] = 0
    return quant_por_estado

def questao_7(caminho = "chagas2018.csv"):
    df = pd.read_csv(caminho)
    cidades_por_uf = {"AC":22, "AL":102, "AP":16, "AM":62, "BA":417, "CE":184,
                      "DF":1, "ES":78, "GO":246, "MA":217, "MT":141, "MS":79,
                      "MG":853, "PA":144, "PB":223, "PR":399, "PE":185,
                      "PI":224, "RN":167, "RS":497, "RJ":91, "RO":52, "RR":15,
                      "SC":295, "SP":645, "SE":75, "TO":139}
    proporcao_por_uf = dict()
    df["SG_UF_NOT"] = df["SG_UF_NOT"].replace(dicionario_estados)
    combinacoes = df.groupby(["SG_UF_NOT", "ID_MUNICIP"]).size().to_frame().reset_index()
    cidades_apareceram = combinacoes["SG_UF_NOT"].value_counts().to_dict()
    for estado in cidades_por_uf.keys():
        if estado in cidades_apareceram.keys():
            proporcao_por_uf[estado] = cidades_apareceram[estado]/cidades_por_uf[estado]
        else:
            proporcao_por_uf[estado] = 0.0
    return proporcao_por_uf

def questao_8(caminho = "chagas2018.csv"):
    df = pd.read_csv(caminho)
    df = df.astype({"DT_NOTIFIC": str, "DT_SIN_PRI": str}).copy()
    df["DT_NOTIFICACAO"] = pd.to_datetime(df["DT_NOTIFIC"])
    df["DT_SINTOMAS"] = pd.to_datetime(df["DT_SIN_PRI"])
    df["ATRASO_NOT"] = (df["DT_NOTIFICACAO"] - df["DT_SINTOMAS"]).dt.days
    return df[["DT_NOTIFICACAO", "DT_SINTOMAS", "ATRASO_NOT"]]

def questao_9(caminho = "chagas2018.csv"):
    df = pd.read_csv(caminho)
    medias_e_desvios = dict()
    df["SG_UF_NOT"] = df["SG_UF_NOT"].replace(dicionario_estados)
    df = df.astype({"DT_NOTIFIC": str, "DT_SIN_PRI": str}).copy()
    df["DT_NOTIFICACAO"] = pd.to_datetime(df["DT_NOTIFIC"])
    df["DT_SINTOMAS"] = pd.to_datetime(df["DT_SIN_PRI"])
    df["ATRASO_NOT"] = (df["DT_NOTIFICACAO"] - df["DT_SINTOMAS"]).dt.days
    media_atrasos = df.groupby("SG_UF_NOT")["ATRASO_NOT"].mean().to_dict()
    desvio_atrasos = df.groupby("SG_UF_NOT")["ATRASO_NOT"].std().to_dict()
    for estado in dicionario_estados.values():
        if estado in media_atrasos:
            medias_e_desvios[estado] = (media_atrasos[estado], desvio_atrasos[estado])
        else:
            medias_e_desvios[estado] = (0, 0)
    return medias_e_desvios

def questao_10(caminho = "chagas2018.csv"):
    df = pd.read_csv(caminho)
    df = df.astype({"DT_NOTIFIC": str, "DT_SIN_PRI": str}).copy()
    df["DT_NOTIFICACAO"] = pd.to_datetime(df["DT_NOTIFIC"])
    df["DT_SINTOMAS"] = pd.to_datetime(df["DT_SIN_PRI"])
    df["ATRASO_NOT"] = (df["DT_NOTIFICACAO"] - df["DT_SINTOMAS"]).dt.days
    media_atraso_mun = df.groupby(["ID_MUNICIP"])["ATRASO_NOT"].mean()
    media_atraso_mun_df = media_atraso_mun.to_frame().reset_index()
    casos_por_municipio = df["ID_MUNICIP"].value_counts().to_frame(name = "NUM_CASOS").rename_axis("ID_MUNICIP").reset_index()
    dataframe_plot = pd.merge(media_atraso_mun_df, casos_por_municipio, on = "ID_MUNICIP")
    dataframe_plot.plot.scatter(
        x="NUM_CASOS",
        y="ATRASO_NOT",
        title="Quantidade de Casos por Média de Atraso de Notificação por Município",
        xlabel="Número de Casos",
        ylabel = "Média de Atraso de Notificação",
        color="red"
    )
    return media_atraso_mun

