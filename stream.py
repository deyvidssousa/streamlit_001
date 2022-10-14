import streamlit as st
import pandas as pd

st.write("""
# Primeiro App
Olá *mundo!*
""")


file = st.file_uploader("Selecione um arquivo")

st.line_chart(file)

#print('ok')