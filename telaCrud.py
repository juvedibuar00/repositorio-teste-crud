import streamlit as st
st.title("Meu título")
st.write("Olá, mundão")
esolha = st.selectbox('Selecione o turno de interesse', ['Manhã', 'Tarde','Noite'])
#Textos renderizados
if esolha:
    st.write(esolha)
radio = ("Selecione uma opção", ['Manhã', 'Tarde','Noite'])
texto = st.text_input('Digite seu nme: ')
numero = st.number_input('Digite um numero')
if texto and numero:
    st.write(texto, numero)

cpf = st.text_input('Digite seu CPF', placeholder='000.000.000-00')

btnCadastrar = st.button('Cadastrar')
st.write(btnCadastrar)

textoLongo = st.text_area('Digite sua reclamação', placeholder='Leave your message here...')