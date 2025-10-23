import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Carregando os dados
@st.cache_data
def carregar_dados():
    url = "https://raw.githubusercontent.com/acidBits/Hello_world_app/main/movies.csv"
    df = pd.read_csv(url)
    df = df.dropna(subset=['generos', 'titulo'])  # Garante que não haja valores nulos
    return df

df = carregar_dados()


# Lista de gêneros únicos
generos_series = df['generos'].apply(lambda x: [g.strip() for g in x.split(',')])
generos_unicos = sorted(set(g for sublist in generos_series for g in sublist))
generos_unicos.insert(0, "")  # opção vazia

# Interface
st.title("🎬 Me Indique um Filme")
st.write("Escolha até 3 gêneros para receber recomendações:")

col1, col2, col3 = st.columns(3)
with col1:
    genero1 = st.selectbox("Gênero 1", generos_unicos, key="g1")
with col2:
    genero2 = st.selectbox("Gênero 2", generos_unicos, key="g2")
with col3:
    genero3 = st.selectbox("Gênero 3", generos_unicos, key="g3")

# Gêneros selecionados
generos_escolhidos = [g for g in [genero1, genero2, genero3] if g]
entrada_usuario = ", ".join(generos_escolhidos)

# Recomendar filmes
if st.button("🔍 Pesquisar"):

