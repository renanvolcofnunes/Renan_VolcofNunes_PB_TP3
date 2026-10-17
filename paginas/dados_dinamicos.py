import streamlit as st
from pathlib import Path

st.title("Dados Dinâmicos sobre Juventude")

BASE = Path(__file__).resolve().parent.parent
ARQUIVO = BASE / "data" / "processed" / "painel_juventudes_trabalho.txt"

st.write("Dados complementares coletados com Selenium a partir do Painel das Juventudes da Bahia.")

if ARQUIVO.exists():
    texto = ARQUIVO.read_text(encoding="utf-8")

    st.subheader("Conteúdo Coletado")
    st.text(texto)

    st.caption("Fonte: Painel das Juventudes da Bahia.")
else:
    st.warning("Execute primeiro a coleta dinâmica com Selenium.")