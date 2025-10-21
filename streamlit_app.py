import streamlit as st

st.title("Me Indique um Filme")

genero1 = ["","norte","Sul","Leste","Oeste"]
select = st.selectbox("Escolha uma Direção:",genero1)
select = st.selectbox("Escolha uma Direção:",genero1)
select = st.selectbox("Escolha uma Direção:",genero1)
st.button("Pesquisar")
st.write(
    f"Voce escolheu a direção:{select}"
)
