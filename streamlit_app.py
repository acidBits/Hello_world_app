import streamlit as st

st.title("Me Indique um Filme")

genero1 = ["","norte","Sul","Leste","Oeste"]
genero2 = ["","norte","Sul","Leste","Oeste"]
genero3 = ["","norte","Sul","Leste","Oeste"]

genero1 = st.selectbox("Escolha uma Direção:",genero1)
genero2 = st.selectbox("escolha",["", "1","2"])
genero3 = st.selectbox("",genero3)

st.button("Pesquisar")
st.write(
    f"Voce escolheu a direção:{genero1}"
)
