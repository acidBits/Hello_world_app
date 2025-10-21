import streamlit as st
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

url = "https://raw.githubusercontent.com/acidBits/Hello_world_app/refs/heads/main/movies.csv"
df = pd.read_csv(url)

st.title("Me Indique um Filme 🎬")
st.divider()

genero = ["","Terror","Comedy","Romance","Action"]

genero1 = st.selectbox("Genero-1:",genero)
genero2 = st.selectbox("Genero-2:",genero)
genero3 = st.selectbox("Genero-3:",genero)

st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("Pesquisar"):
    st.write()

