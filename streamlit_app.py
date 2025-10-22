import streamlit as st
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

url = "https://raw.githubusercontent.com/acidBits/Hello_world_app/refs/heads/main/movies.csv"
df = pd.read_csv(url)

# Inicializando o vetorizador
#vectorizer = TfidfVectorizer()
#X = vectorizer.fit_transform(df['generos'])
# Tratando os gêneros: separando por vírgula e limpando espaços
generos_series = df['generos'].dropna().apply(lambda x: [g.strip() for g in x.split(',')])

# Achata a lista e extrai os únicos
generos_unicos = sorted(set(g for sublist in generos_series for g in sublist))
generos_unicos.insert(0,"")


st.title("Me Indique um Filme 🎬")
st.divider()

genero1 = st.selectbox("Genero-1:",generos_unicos)
genero2 = st.selectbox("Genero-2:",generos_unicos)
genero3 = st.selectbox("Genero-3:",generos_unicos)

generos_agrupados = f"{genero1},{genero2},{genero3}"


st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("Pesquisar"):
    st.write(generos_agrupados)

