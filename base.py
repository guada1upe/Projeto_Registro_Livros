import mysql.connector

conectar = mysql.connector.connect(host ='localhost', database = 'Sistema_Registro_Livros', user='root', password = 'teste@123')

print('Bem-vindo a nossa biblioteca!')

print('O que você deseja fazer?  \n 1 -> Pesquisar livro pelo título; \n 2 -> Cadastrar novos livros; \n 3 -> Deletar livro; \n 4 -> Mostrar tabela de livros.')
escolha = int(input('Digite: '))

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

def mostrar():
    ComandoSelect = 'SELECT * FROM tbRegistros_Livros;'

    cursor = conectar.cursor()
    cursor.execute(ComandoSelect)
    retornoDeDados = cursor.fetchall()

    print('-------------------------------------------------------------------')
    for i in retornoDeDados:
        print(f'Id_Livro: {i[0]}, Titulo: {i[1]}, Autor: {i[2]}, Genero: {i[3]}')
    cursor.close()

mostrar()