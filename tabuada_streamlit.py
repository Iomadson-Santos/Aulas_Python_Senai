import streamlit as st


st.title("Tabuada Simples 🧮")
st.subheader("Feito com Streamlit ❤️")

numero_tabuada = st.number_input("Digite o multiplicador da tabuada",0)
inicio_tabuada = st.number_input("Digite o inicia da tabuada",0)
final_tabuada = st.number_input("Digite o final da tabuada",0)

if st.button("calcular"):
    for multiplicador in range(inicio_tabuada,final_tabuada+1):
        #st.text(f"{numero_tabuada} X {multiplicador} = {multiplicador*numero_tabuada}")#
        st.markdown(f"**{numero_tabuada} X {multiplicador} = {multiplicador*numero_tabuada}**")