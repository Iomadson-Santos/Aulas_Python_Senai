import streamlit as st

st.title("Calculadora simples 🦞")
st.subheader("Feito com StreamLit 💖")

valor1=st.number_input("Digite o primeiro valor: ",0)
valor2=st.number_input("Digite o segundo valor: ",0)

opcao = st.selectbox(
    "Qual operação deseja realiza: ",
    ("Soma","Subtração","Multiplicação","Divisão"))


if st.button("Calcular"):
    st.success(f"{valor1+valor2}")