import streamlit as st
from excel_parser import parse_excel
from agent import analyze_document

st.set_page_config(page_title="Agent IA – Hygiène documentaire", layout="wide")

st.title("🧠 Agent IA – Gestion documentaire hygiène")

uploaded_file = st.file_uploader(
    "Uploader un fichier Excel (.xlsx)",
    type=["xlsx", "xls"]
)

if uploaded_file:
    with st.spinner("Lecture du fichier Excel..."):
        text = parse_excel(uploaded_file)

    st.success("Fichier Excel lu")

    with st.spinner("Analyse IA en cours..."):
        result = analyze_document(text)

    st.subheader("Résultat de l’analyse")
    st.write(result)
