import streamlit as st

st.title("Sobre o Projeto")

st.subheader("Fontes e Referências")

st.markdown(
    """
    - [IBGE / SIDRA](https://sidra.ibge.gov.br/)
    - [Ministério do Trabalho e Emprego](https://www.gov.br/trabalho-e-emprego/)
    - [Conecta Brasil](https://conectabrasil.org/home)
    - [Observatório do Terceiro Setor](https://observatorio3setor.org.br/)
    - [Agência Brasil](https://agenciabrasil.ebc.com.br/)
    """
)

st.subheader("Evolução para o TP3")

st.write("Nesta etapa, a aplicação foi reorganizada em múltiplas páginas para separar as diferentes funcionalidades e análises.")

st.write("O projeto também será integrado a uma API desenvolvida com FastAPI e preparado para futuras funcionalidades utilizando LLMs.")