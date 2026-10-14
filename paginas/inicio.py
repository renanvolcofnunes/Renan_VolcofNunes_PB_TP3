import streamlit as st

st.title("Empregabilidade Jovem no Brasil")

st.subheader("Problema de Negócio")

st.write(
    """
    O projeto busca analisar os desafios relacionados à empregabilidade de jovens no Brasil,
    identificando diferenças entre regiões e compreendendo quais competências profissionais
    aparecem com maior frequência nas oportunidades de trabalho.
    """
)

st.subheader("Objetivos do Projeto")

st.markdown(
    """
    - Comparar indicadores de empregabilidade jovem entre estados e regiões brasileiras.
    - Identificar regiões com maiores desafios de inserção dos jovens no mercado de trabalho.
    - Identificar competências profissionais recorrentes nas oportunidades de trabalho.
    - Apresentar os resultados de forma organizada em um dashboard interativo.
    """
)

st.subheader("Navegação")

st.page_link("paginas/indicadores.py", label="Indicadores de Empregabilidade")
st.page_link("paginas/comparador.py", label="Comparador de Estados")
st.page_link("paginas/noticias.py", label="Notícias sobre Empregabilidade")
st.page_link("paginas/sobre.py", label="Sobre o Projeto")