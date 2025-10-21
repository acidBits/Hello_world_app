import streamlit as st

st.title("Me Indique um Filme 🎥🎬")
st.divider()

genero1 = ["","norte","Sul","Leste","Oeste"]
genero2 = ["","norte","Sul","Leste","Oeste"]
genero3 = ["","norte","Sul","Leste","Oeste"]

genero1 = st.selectbox("Genero-1:",genero1)
genero2 = st.selectbox("Genero-2:",genero2)
genero3 = st.selectbox("Genero-3:",genero3)

if st.button("Pesquisar"):
    st.write(f"A direção Indicada é: {genero1}")

