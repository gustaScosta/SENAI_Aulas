import streamlit as st 
import pandas as pd

st.title('Aula 18 - Pacotes e Frameworks')


class livro():
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def cadastroar_livro(self):
        st.write(f"Livro cadastrado: {self.titulo} - {self.autor} ({self.ano})")
        return self.titulo, self.autor, self.ano
    
nome = st.text_input("Digite o nome do livro:")
autor = st.text_input("Digite o nome do autor:")
ano = st.number_input("Digite o ano de publicação:", min_value=0, max_value=2026, step=1)
if st.button("Cadastrar Livro"):
    livro_cadastrado = livro(nome, autor, ano)
    livro_cadastrado.cadastroar_livro()