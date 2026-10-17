import streamlit as st
from comum import inicializar_estado, preservar_estado

st.set_page_config(page_title="Empregabilidade Jovem no Brasil", layout="wide")

inicializar_estado()
preservar_estado()

pagina = st.navigation({"Painel": [st.Page("paginas/inicio.py", title="Início", default=True), st.Page("paginas/indicadores.py", title="Indicadores"),
                                  st.Page("paginas/comparador.py", title="Comparador"), st.Page("paginas/noticias.py", title="Notícias"),
                                  st.Page("paginas/dados_dinamicos.py", title="Dados Dinâmicos"), st.Page("paginas/api.py", title="API")],
                        "Projeto": [st.Page("paginas/sobre.py", title="Sobre o projeto")]})

pagina.run()