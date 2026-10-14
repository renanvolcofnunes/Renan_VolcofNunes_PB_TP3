import streamlit as st

from comum import carregar_dados, ARQUIVO

st.title("Comparador de Estados")

dados = carregar_dados(ARQUIVO)

opcoes_estados = {
    linha["estado"]: linha["uf"]
    for linha in dados
}

estado_comparacao = st.selectbox("Selecione um estado para adicionar à comparação:", list(opcoes_estados.keys()))

if st.button("Adicionar à comparação"):
    uf = opcoes_estados[estado_comparacao]

    if uf not in st.session_state.ufs_comparacao:
        st.session_state.ufs_comparacao.append(uf)

if st.button("Limpar comparação"):
    st.session_state.ufs_comparacao = []

dados_comparacao = [
    linha for linha in dados
    if linha["uf"] in st.session_state.ufs_comparacao
]

if dados_comparacao:
    st.write("Estados selecionados para comparação:")
    st.dataframe(dados_comparacao, width="stretch")
    st.bar_chart(dados_comparacao, x="estado", y="taxa_desocupacao")
else:
    st.info("Selecione um estado e clique em 'Adicionar à comparação'.")