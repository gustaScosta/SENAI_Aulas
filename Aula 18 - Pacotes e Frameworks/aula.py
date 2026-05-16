import streamlit as st
import pandas as pd

st.title('Aula 18 - Pacotes e Frameworks')


class livro():
    def __init__(self, titulo, autor, data_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.data_publicacao = data_publicacao

    def cadastroar_livro(self):
        data_formatada = self.data_publicacao.strftime("%d/%m/%Y")
        st.write(f"Livro cadastrado: {self.titulo} - {self.autor} ({data_formatada})")
        return self.titulo, self.autor, self.data_publicacao


nome = st.text_input("Digite o nome do livro:")
autor = st.text_input("Digite o nome do autor:")
data_publicacao = st.date_input(
    "Digite a data de publicacao:",
    value=pd.Timestamp("2023-01-01"),
    format="DD/MM/YYYY"
)

if st.button("Cadastrar Livro"):
    livro_cadastrado = livro(nome, autor, data_publicacao)
    livro_cadastrado.cadastroar_livro()
