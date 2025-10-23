import streamlit as st
import pandas as pd
import joblib
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Carregando os dados
url = "https://raw.githubusercontent.com/acidBits/Hello_world_app/refs/heads/main/movies.csv"
df = pd.read_csv(url)

#carregando modelo
url = "https://github.com/acidBits/Hello_world_app/blob/main/vectorizer_model.pkl"
r = requests.get(url)
X = joblib.load("vectorizer_model.pkl")

# Tratando os gêneros: separando por vírgula e limpando espaços
generos_series = df['generos'].dropna().apply(lambda x: [g.strip() for g in x.split(',')])

# Achata a lista e extrai os únicos
generos_unicos = sorted(set(g for sublist in generos_series for g in sublist))
generos_unicos.insert(0,"")


#
vectorizer = TfidfVectorizer()


def recomendar_por_genero(generos_agrupados, df, vectorizer, X):
    # Vetor do gênero informado pelo usuário
    genero_vetor = vectorizer.transform([generos_usuario])

    # Calculando similaridade entre o input e os filmes
    similaridade = cosine_similarity(genero_vetor, X)[0]

    # Ordenando os filmes com maior similaridade
    df['similaridade'] = similaridade
    recomendacoes = df.sort_values(by=['similaridade','pontuacao'], ascending=False).head()
   
    return recomendacoes[['filme','pontuacao','ano', 'generos', 'similaridade']].reset_index(drop=True)


def ao_clicar()
generos_agrupados = f"{genero1},{genero2},{genero3}"
recomendacoes = recomendar_por_genero(generos_agrupados, df, vectorizer, X)

st.title("Me Indique um Filme 🎬")
st.divider()

genero1 = st.selectbox("Genero-1:",generos_unicos)
genero2 = st.selectbox("Genero-2:",generos_unicos)
genero3 = st.selectbox("Genero-3:",generos_unicos)

generos_agrupados = f"{genero1},{genero2},{genero3}"


st.markdown("<br><br>", unsafe_allow_html=True)
if st.button("Pesquisar"):
    ao_clicar()
    st.write(recomendacoes)
    

