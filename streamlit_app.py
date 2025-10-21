import streamlit as st

st.title("Meu Aplicativo")
st.write(
    "Testando meu aplicativo"
)

opcoes = ["norte","Sul","Leste","Oeste"]
select = st.selectbox("Escolha uma Direção:",opcoes)
st.write(
    f"Voce selecionou:{select}"
)
