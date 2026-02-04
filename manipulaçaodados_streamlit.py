import streamlit as st

st.title("Cadastro de Cliente 😉")
st.subheader("Feito com STREAMLIT 💻")

nome = st.text_input("Digite seu nome: ")
idade = st.number_input("Digite sua idade: ",0)
email = st.text_input("Digite seu e-mail: ")
senha = st.text_input("Digite sua senha", type="password")
confirmacao = st.text_input("Confirme sua senha", type="password")

if st.button("Cadastrar"):
    with open("./pessoa.txt", "a") as arquivo:
        arquivo.write(f"Nome:{nome:<15} | Idade: {idade:<4} | E-MAIL:{email:<20}\n")
        st.toast("Cadastrado com sucess!", icon="😉")