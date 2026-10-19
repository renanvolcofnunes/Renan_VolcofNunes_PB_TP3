import streamlit as st
from fastapi.testclient import TestClient
from api.main import app

cliente = TestClient(app)

st.title("Integração com a API")

st.write("Esta página utiliza a API FastAPI desenvolvida no projeto para consultar indicadores e enviar notícias.")

st.subheader("Consultar Indicadores")

ufs = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
uf = st.selectbox("Selecione uma UF:", ufs)

if st.button("Consultar API"):
    resposta = cliente.get(f"/indicadores/{uf}")
    dados = resposta.json()

    st.success("Consulta realizada com sucesso!")
    st.write("Quantidade de registros:", dados["quantidade"])
    st.dataframe(dados["dados"], width="stretch")

st.subheader("Enviar Nova Notícia")

with st.form("form_noticia"):
    titulo = st.text_input("Título:")
    data = st.text_input("Data:", placeholder="2026-10-19")
    url = st.text_input("URL:")
    fonte = st.text_input("Fonte:")
    enviar = st.form_submit_button("Enviar notícia para API")

    if enviar:
        noticia = {"titulo": titulo, "data": data, "url": url, "fonte": fonte}
        resposta = cliente.post("/noticias", json=noticia)

        if resposta.status_code == 201:
            st.success("Notícia enviada para a API com sucesso!")
            st.json(resposta.json())
        else:
            st.error("A API recusou os dados enviados.")
            st.json(resposta.json())

st.subheader("Notícias Recebidas pela API")

if st.button("Consultar notícias da API"):
    resposta = cliente.get("/noticias")
    dados = resposta.json()

    st.write("Quantidade de notícias:", dados["quantidade"])

    if dados["dados"]:
        st.dataframe(dados["dados"], width="stretch")
    else:
        st.info("Nenhuma notícia foi enviada pela API.")