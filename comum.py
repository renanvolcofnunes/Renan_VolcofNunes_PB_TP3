import csv
import streamlit as st
from pathlib import Path

BASE = Path(__file__).resolve().parent

ARQUIVO = BASE / "data" / "sample" / "empregabilidade_jovem.csv"
ARQUIVO_NOTICIAS = BASE / "data" / "processed" / "noticias_empregabilidade.csv"

@st.cache_data(ttl=600)
def carregar_dados(caminho):
    dados = []

    with open(caminho, "r", encoding="utf-8-sig") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            linha["taxa_desocupacao"] = float(linha["taxa_desocupacao"])
            dados.append(linha)

    return dados

@st.cache_data(ttl=600)
def carregar_noticias(caminho):
    noticias = []

    if caminho.exists():
        with open(caminho, "r", encoding="utf-8-sig") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                noticias.append(linha)

    return noticias

def inicializar_estado():
    if "ufs_comparacao" not in st.session_state:
        st.session_state.ufs_comparacao = []

    if "noticias_enviadas" not in st.session_state:
        st.session_state.noticias_enviadas = []

    if "arquivos_enviados" not in st.session_state:
        st.session_state.arquivos_enviados = []

def preservar_estado():
    chaves = ["ufs_comparacao", "noticias_enviadas", "arquivos_enviados", "regiao_filtro", "estado_filtro"]

    for chave in chaves:
        if chave in st.session_state:
            st.session_state[chave] = st.session_state[chave]