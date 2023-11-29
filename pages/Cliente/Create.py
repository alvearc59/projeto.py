import streamlit as st;
import controllers.ClienteController as ClienteController
import models.Cliente as cliente
import pages.Cliente.Edit as pageConsulditCliente



def IncluirClientePage():
    idAlteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    clienteRecuperado = None 
    if idAlteracao.get("id") != None:
       st.experimental_set_query_params()
       idAlteracao = idAlteracao.get("id")[0]
       clienteRecuperado = ClienteController.selecionarByid(idAlteracao)
       st.experimental_set_query_params(
           id=[clienteRecuperado.nome_aluno]
       )
       st.write(idAlteracao)
       st.title("Alterar Aluno")

    else:
       st.title("Adicionar Aluno")

    with st.form(key="incluir_cliente"):
       listOcupation = ["Desenvolvedor","Designer","Professor","Astronauta","Mecânico","Instrutor de Voo"]
       if clienteRecuperado == None:
            input_name = st.text_input(label="Insira o seu nome")
            input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
            input_occupation = st.selectbox(label ="Selecione sua profissão",options=listOcupation)
            
       else:
            input_name = st.text_input(label="Insira o seu nome", value = clienteRecuperado.nome_aluno)
            input_age = st.number_input(label="Insira sua idade", format="%d", step=1, value = clienteRecuperado.data_nascimento)
            input_occupation = st.selectbox(label ="Selecione sua profissão",options=listOcupation, index=listOcupation.index(clienteRecuperado.sala_aluno))
       input_button_submit = st.form_submit_button("Enviar")
          

  
    if input_button_submit:
      if clienteRecuperado == None:
         ClienteController.incluir(cliente.Cliente(input_name,input_age,input_occupation))
         st.success("Aluno Incluido com sucesso!")
      else:
          st.experimental_set_query_params()
          ClienteController.alterar(cliente.Cliente(input_name,input_age,input_occupation))
          st.success("Aluno alterado com sucesso!")
          
      
