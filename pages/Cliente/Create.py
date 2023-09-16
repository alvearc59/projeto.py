import streamlit as st;
import controllers.ClienteController as ClienteController
import models.Cliente as cliente


def IncluirClientePage():
    st.title("Adicionar Alunos")
    with st.form(key="include_cliente"):
        input_name = st.text_input(label="Insira o seu nome")
        input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
        input_occupation = st.selectbox("Selecione sua profissão",["Desenvolvedor","Designer","Professor","Astronauta","Mecânico","Instrutor de Voo"])
        input_button_submit = st.form_submit_button("Enviar")
    
  
    if input_button_submit:
      ClienteController.incluir(cliente.Cliente(input_name,input_age,input_occupation))
      st.success("Aluno Incluido com sucesso!")
