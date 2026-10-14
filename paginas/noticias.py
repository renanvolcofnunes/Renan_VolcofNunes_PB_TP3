import csv
import re
import io
import hashlib
import streamlit as st
from collections import Counter

from comum import carregar_noticias, ARQUIVO_NOTICIAS

st.title("Notícias sobre Empregabilidade Jovem")

noticias = carregar_noticias(ARQUIVO_NOTICIAS)

if noticias:
    st.write("Quantidade de notícias coletadas:", len(noticias))
    st.dataframe(noticias, width="stretch")

    for noticia in noticias:
        st.markdown(f"**{noticia['titulo']}**")
        st.write("Data:", noticia["data"][:10])
        st.write("Fonte:", noticia["fonte"])
        st.markdown(f"[Ler notícia completa]({noticia['url']})")
        st.divider()

    st.subheader("Palavras mais frequentes nas notícias")

    texto = " ".join(noticia["titulo"] for noticia in noticias)
    texto = texto.lower()

    palavras = re.findall(r"[a-zà-ÿ]{4,}", texto)

    palavras_vazias = ["para", "como", "entre", "mais", "menos", "sobre", "pela", "pelos", "pelas", "com", "uma", "esse", "essa"]

    palavras_filtradas = [
        palavra for palavra in palavras
        if palavra not in palavras_vazias
    ]

    contagem = Counter(palavras_filtradas)
    mais_frequentes = contagem.most_common(10)

    frequencias = []

    for palavra, quantidade in mais_frequentes:
        frequencias.append({"palavra": palavra, "frequencia": quantidade})

    if frequencias:
        st.bar_chart(frequencias, x="palavra", y="frequencia")
else:
    st.warning("O arquivo de notícias não foi encontrado.")

st.subheader("Adicionar Notícias Complementares")

st.write("Envie um arquivo CSV com notícias sobre empregabilidade para complementar as informações do dashboard.")

def validar_csv_noticias(conteudo):
    if not conteudo:
        return [], "O arquivo enviado está vazio."

    texto = None

    for codificacao in ["utf-8-sig", "utf-8", "latin-1"]:
        try:
            texto = conteudo.decode(codificacao)
            break
        except UnicodeDecodeError:
            continue

    if texto is None:
        return [], "Não foi possível ler o arquivo."

    try:
        leitor = csv.DictReader(io.StringIO(texto), strict=True)

        if leitor.fieldnames is None:
            return [], "O CSV não possui cabeçalho."

        colunas_obrigatorias = ["titulo", "data", "url", "fonte"]

        faltantes = [
            coluna for coluna in colunas_obrigatorias
            if coluna not in leitor.fieldnames
        ]

        if faltantes:
            return [], "Faltam colunas obrigatórias: " + ", ".join(faltantes)

        linhas = []

        for linha in leitor:
            noticia = {}

            for coluna in colunas_obrigatorias:
                valor = linha.get(coluna)

                if valor is None or not valor.strip():
                    return [], f"A coluna '{coluna}' contém um valor vazio."

                noticia[coluna] = valor.strip()

            noticia["procedencia"] = "Upload"
            linhas.append(noticia)

        if not linhas:
            return [], "O CSV não possui notícias."

        return linhas, None

    except (csv.Error, UnicodeError, ValueError):
        return [], "Não foi possível interpretar o arquivo CSV."

arquivo_enviado = st.file_uploader("Selecione um arquivo CSV:", type="csv")

if arquivo_enviado is not None:
    conteudo = arquivo_enviado.getvalue()

    st.write("Arquivo:", arquivo_enviado.name)
    st.write("Tamanho:", len(conteudo), "bytes")

    if len(conteudo) > 2000000:
        st.error("O arquivo deve ter no máximo 2 MB.")
    else:
        linhas, erro = validar_csv_noticias(conteudo)

        if erro:
            st.error(erro)
        else:
            st.success(f"Arquivo válido: {len(linhas)} notícias identificadas.")

            if st.button("Adicionar notícias ao dashboard"):
                identificador = hashlib.sha256(conteudo).hexdigest()

                if identificador in st.session_state.arquivos_enviados:
                    st.warning("Este arquivo já foi adicionado.")
                else:
                    st.session_state.noticias_enviadas.extend(linhas)
                    st.session_state.arquivos_enviados.append(identificador)
                    st.success("Notícias adicionadas com sucesso!")

if st.session_state.noticias_enviadas:
    st.subheader("Notícias Adicionadas pelo Usuário")

    st.dataframe(st.session_state.noticias_enviadas, width="stretch")

    if st.button("Limpar notícias enviadas"):
        st.session_state.noticias_enviadas = []
        st.session_state.arquivos_enviados = []
        st.rerun()

st.subheader("Análise Conjunta das Notícias")

noticias_completas = []
urls_adicionadas = []

for noticia in noticias + st.session_state.noticias_enviadas:
    url = noticia["url"].strip()

    if url not in urls_adicionadas:
        urls_adicionadas.append(url)

        linha = dict(noticia)

        if "procedencia" not in linha:
            linha["procedencia"] = "Coleta Web"

        noticias_completas.append(linha)

st.write("Quantidade total de notícias:", len(noticias_completas))

if noticias_completas:
    st.dataframe(noticias_completas, width="stretch")

    texto_completo = " ".join(noticia["titulo"] for noticia in noticias_completas)
    texto_completo = texto_completo.lower()

    palavras = re.findall(r"[a-zà-ÿ]{4,}", texto_completo)

    palavras_vazias = ["para", "como", "entre", "mais", "menos", "sobre", "pela", "pelos", "pelas", "com", "uma", "esse", "essa"]

    palavras_filtradas = [
        palavra for palavra in palavras
        if palavra not in palavras_vazias
    ]

    contagem = Counter(palavras_filtradas)
    mais_frequentes = contagem.most_common(10)

    frequencias = []

    for palavra, quantidade in mais_frequentes:
        frequencias.append({"palavra": palavra, "frequencia": quantidade})

    st.subheader("Palavras mais frequentes na análise conjunta")

    if frequencias:
        st.bar_chart(frequencias, x="palavra", y="frequencia")
    else:
        st.info("Não há palavras disponíveis para análise.")
else:
    st.info("Não há notícias disponíveis para análise.")