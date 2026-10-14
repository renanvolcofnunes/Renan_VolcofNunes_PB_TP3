import csv
import io
import streamlit as st

from comum import carregar_dados, ARQUIVO

st.title("Indicadores de Empregabilidade")

dados = carregar_dados(ARQUIVO)

st.subheader("Filtros de Empregabilidade")

regioes = ["Todas"] + sorted(set(linha["regiao"] for linha in dados))

if "regiao_filtro" not in st.session_state:
    st.session_state.regiao_filtro = "Todas"

regiao_selecionada = st.selectbox("Selecione uma região:", regioes, key="regiao_filtro")

if regiao_selecionada == "Todas":
    dados_regiao = dados
else:
    dados_regiao = [linha for linha in dados if linha["regiao"] == regiao_selecionada]

estados = ["Todos"] + sorted(set(linha["estado"] for linha in dados_regiao))

if "estado_filtro" not in st.session_state or st.session_state.estado_filtro not in estados:
    st.session_state.estado_filtro = "Todos"

estado_selecionado = st.selectbox("Selecione um estado:", estados, key="estado_filtro")

if estado_selecionado == "Todos":
    dados_filtrados = dados_regiao
else:
    dados_filtrados = [linha for linha in dados_regiao if linha["estado"] == estado_selecionado]

st.subheader("Resultados da Consulta")

st.write("Quantidade de registros:", len(dados_filtrados))
st.dataframe(dados_filtrados, width="stretch")

st.subheader("Taxa de Desocupação dos Jovens por Estado")

st.write("Comparação da taxa de desocupação dos jovens de 18 a 24 anos entre os estados brasileiros.")

if dados_filtrados:
    st.bar_chart(dados_filtrados, x="estado", y="taxa_desocupacao")
else:
    st.warning("Não há dados disponíveis para os filtros selecionados.")

st.subheader("Download dos Indicadores")

if dados_filtrados:
    arquivo_saida = io.StringIO()
    campos = list(dados_filtrados[0].keys())
    escritor = csv.DictWriter(arquivo_saida, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(dados_filtrados)

    st.download_button(label="Baixar indicadores em CSV", data=arquivo_saida.getvalue().encode("utf-8-sig"), file_name="indicadores_empregabilidade.csv", mime="text/csv")
else:
    st.info("Não há dados disponíveis para download.")