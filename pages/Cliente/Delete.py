import streamlit as st;
import controllers.ClienteController as ClienteController
import pandas as pd

from unittest import main
import  pages.Cliente.Create as pageCreateCliente



def ExcluirClienteDelete():
    paramId = st.experimental_get_query_params()
    if paramId == {}:
       st.experimental_set_query_params()
       st.title("Excluir  Alunos")
       colmns = st.columns((1,1,1,1,1))
       campos = ["Nome", "Idade","Profissão", "Excluir", "Alterar"]
       for col, campo_nome in zip(colmns, campos):
          col.write(campo_nome)
    
       for item in ClienteController.selecionarTodos():
          col1, col2, col3, col4,col5 = st.columns((1,1,1,1,1))
          col1.write(item.nome_aluno)
          col2.write(item.data_nascimento)
          col3.write(item.sala_aluno)
          button_space_excluir = col4.empty()
          on_click_excluir = button_space_excluir.button("Excluir", "BtnExluir" + str(item.nome_aluno))
          button_space_alterar = col5.empty()
          on_click_alterar = button_space_alterar.button("Alterar","btnAlterar" + str(item.nome_aluno))


          if on_click_excluir:
            ClienteController.Excluir(item.nome_aluno)
            button_space_excluir.button(
            "Excluído", "Btexcluir" + str(item.nome_aluno))
            st.success("Aluno eliminado  com sucesso!")

          if on_click_alterar:
            st.experimental_set_query_params(
            id=[item.nome_aluno]
            )
            st.experimental_rerun()
    else:
       on_click_voltar = st.button("Voltar")
       if on_click_voltar:
          st.experimental_set_query_params()
          st.experimental_rerun
       pageCreateCliente.IncluirClientePage()
       
           



     