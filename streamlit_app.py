import streamlit as st

st.title("Me Indique um Filme")

genero1 = ["","norte","Sul","Leste","Oeste"]
genero2 = ["","norte","Sul","Leste","Oeste"]
genero3 = ["","norte","Sul","Leste","Oeste"]

select1 = st.selectbox("Escolha uma Direção:",genero1)
select2 = st.selectbox("Escolha uma Direção:",genero2)
select3 = st.selectbox("Escolha uma Direção:",genero3)
st.button("Pesquisar")
st.write(
    f"Voce escolheu a direção:{select1}"
)
