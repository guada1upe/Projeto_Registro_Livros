import mysql.connector

conectar = mysql.connector.connect(host ='localhost', database = 'Sistema_Registro_Livros', user='root', password = 'teste@123')

if conectar.is_connected():
    print('Conexão realizado com sucesso!')
else:
    print('falha na conexão')

def cadastro():
    Titulolivro = input ('Informe o titulo do livro que deseja cadastra: ')
    Nomeautor = input ('Informe o autor do livro: ')
    Genero = input (' Informe o Genero do livro: ')

    dados = "" f"('{Titulolivro}', '{Nomeautor}', '{Genero}');"""

    comando_Insert = """insert into tbRegistros_Livros (Titulo, Autor, Genero) values """

    sql = comando_Insert + dados

    cursor = conectar.cursor()
    cursor.execute(sql)
    conectar.commit()
    print('Dados cadastrados! ')

