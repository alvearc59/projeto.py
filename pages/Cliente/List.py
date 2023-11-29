import streamlit as st;
import controllers.ClienteController as ClienteController
import pandas as pd


def List():
    st.experimental_set_query_params()
    st.title("Consulta de Alunos")

    costumerList = []

    for item in ClienteController.selecionarTodos():
        costumerList.append([item.nome_aluno, item.data_nascimento, item.sala_aluno])

    df = pd.DataFrame(
        costumerList,
        columns=['Nome','Data de Nascimento','Sala']
    )

    st.table(df)

