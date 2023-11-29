#Biblioteca   streamlit para criação do FRONT 
from os import write
from typing import List
from numpy.core.fromnumeric import size
from cgitb import text
from multiprocessing import Value
import streamlit as st;
import controllers.ClienteController as ClienteController
import pandas as pd
import pages.Cliente.Create as pageCreateCliente
import pages.Cliente.List as PageListCliente
import pages.Cliente.Delete as pageDeleteCliente
import pages.Cliente.Edit as pageConsulditCliente


st.set_page_config(page_title="Cadastro de Novos Profissionais")
st.title("Cadastro de Novos Profissionais")
st.write("Deseja entrar no Dash do Projeto? [Clique Aqui](https://github.com/users/alvearc59/projects/1/views/1?layout=board)")
st.write("Deseja entrar no código do Projeto? [Clique Aqui](https://github.com/alvearc59/projeto.py)")

#Criando as janelas

st.sidebar.title('Menu')
page_cliente = st.sidebar.selectbox('CLIENTE', ['Criar','Excluir','Consultar'])

if page_cliente == 'Consultar':
    PageListCliente.List()


if page_cliente == 'Criar':
    st.experimental_set_query_params()
    pageCreateCliente.IncluirClientePage()

if page_cliente == 'Excluir':
    pageDeleteCliente.ExcluirClienteDelete()



  