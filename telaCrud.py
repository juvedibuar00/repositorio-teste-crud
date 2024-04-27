import streamlit as st
from funcoesCrud import *
import mysql.connector
st.title("Sistema Dieguinho Alimentos - ME")
st.markdown('## Cadastro de Produtos')
nome = st.text_input('Nome do produto', placeholder='Nome do produto com no máximo 50 caracteres')
imagem = st.text_input('Imagem do produto', placeholder='URL da imagem com até 100 caracteres')
codigo = st.text_input('Código do produto', placeholder='Código do produto')
preco = float(st.number_input('Preço do produto: '))
btnCadastrarProduto = st.button('Cadastrar Produto')
if btnCadastrarProduto:
    cadastrar(nome, preco, codigo, imagem)
    st.write('Produto cadastrado com sucesso!')
