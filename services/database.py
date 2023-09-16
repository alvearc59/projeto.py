import pyodbc


dados_conexao = (
    "Driver={SQL Server};"
    "Server=Moeme;"
    "Database=ALUNO;"
)

cnxn = pyodbc.connect(dados_conexao)
cursor = cnxn.cursor()
