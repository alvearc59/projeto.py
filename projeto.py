#baixei o streamlit para criar a tela do crud
from os import write
from numpy.core.fromnumeric import size
import streamlit as st;
import controllers.ClienteController as ClienteController
import pandas as pd
import pages.Cliente.Create as pageCreateCliente
import pages.Cliente.List as PageListCliente

st.set_page_config(page_title="Cadastro de Novos Profissionais")
st.title("Cadastro de Novos Profissionais")
st.write("Deseja entrar no Dash do Projeto? [Clique Aqui](https://github.com/users/alvearc59/projects/1/views/1?layout=board)")
st.write("Deseja entrar no código do Projeto? [Clique Aqui](https://github.com/alvearc59/projeto.py)")

#Criando as janelas

st.sidebar.title('Menu')
page_cliente = st.sidebar.selectbox('CLIENTE', ['Criar','Alterar','Excluir','Consultar'])

if page_cliente == 'Consultar':
    PageListCliente.List()


if page_cliente == 'Criar':
    pageCreateCliente.IncluirClientePage()
  