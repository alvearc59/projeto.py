import streamlit as st;
import controllers.ClienteController as ClienteController
import pandas as pd


def List():
    st.title("Consulta de Alunos")

    costumerList = []

    for item in ClienteController.selecionarTodos():
        costumerList.append([item.nome_aluno, item.data_nascimento, item.sala_aluno])

    df = pd.DataFrame(
        costumerList,
        columns=['nome_aluno','data_nascimento','sala_aluno']
    )

    st.table(df)