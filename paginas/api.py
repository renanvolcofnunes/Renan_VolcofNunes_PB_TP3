import os
import requests
import streamlit as st

API_URL = os.getenv("EMPREGABILIDADE_API_URL", "http://127.0.0.1:8000")

st.title("Integração com a API")
st.write("Esta página consome a API FastAPI do projeto por meio de requisições HTTP.")
st.subheader("Consultar Indicadores")

ufs = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
uf = st.selectbox("Selecione uma UF:", ufs)

if st.button("Consultar API"):
    try:
        resposta = requests.get(f"{API_URL}/indicadores/{uf}", timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        st.success("Consulta realizada com sucesso!")
        st.write("Quantidade de registros:", dados["quantidade"])
        st.dataframe(dados["dados"], width="stretch")

    except requests.RequestException:
        st.warning("A API não está disponível. Execute o FastAPI com Uvicorn.")

st.subheader("Enviar Nova Notícia")

with st.form("form_noticia"):
    titulo = st.text_input("Título:")
    data = st.text_input("Data:", placeholder="2026-11-14")
    url = st.text_input("URL:")
    fonte = st.text_input("Fonte:")
    enviar = st.form_submit_button("Enviar notícia para API")

    if enviar:
        noticia = {"titulo": titulo, "data": data, "url": url, "fonte": fonte}

        try:
            resposta = requests.post(f"{API_URL}/noticias", json=noticia, timeout=10)

            if resposta.ok:
                st.success("Notícia enviada para a API com sucesso!")
                st.json(resposta.json())
            else:
                st.error("A API recusou os dados enviados.")
                st.json(resposta.json())

        except requests.RequestException:
            st.warning("A API não está disponível. Execute o FastAPI com Uvicorn.")

st.subheader("Notícias Recebidas pela API")

if st.button("Consultar notícias da API"):
    try:
        resposta = requests.get(f"{API_URL}/noticias", timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        st.write("Quantidade de notícias:", dados["quantidade"])

        if dados["dados"]:
            st.dataframe(dados["dados"], width="stretch")
        else:
            st.info("Nenhuma notícia foi enviada pela API.")

    except requests.RequestException:
        st.warning("A API não está disponível. Execute o FastAPI com Uvicorn.")