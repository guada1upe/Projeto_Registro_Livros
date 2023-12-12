import mysql.connector

conectar = mysql.connector.connect(host ='localhost', database = 'Sistema_Registro_Livros', user='root', password = 'teste@123')

def Pesquisar():
    Titulo = input('Qual o título do livro?')
    filtro = """select * from tbRegistros_Livros where Titulo ="""
    sqlFiltro = ""f"{filtro} '{Titulo}' ;"""

    cursor = conectar.cursor()
    cursor.execute(sqlFiltro)
    retornodeDados = cursor.fetchall()
    for i in retornodeDados:
        print(f'Titulo: {i[1]}, \n Autor: {i[2]}')

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

def excluir_livros(self, titulo):
        if titulo in self.catalogo:
             del self.catalogo[titulo]
             print(f"Livro '{titulo}' removido do catalogo.")
        else:
             print(f"Livro '{titulo}' não encontrado no catalogo.")

print('Bem-vindo a nossa biblioteca!')

print('O que você deseja fazer?  \n 1 -> Pesquisar livro pelo título; \n 2 -> Cadastrar novos livros; \n 3 -> Deletar livro; \n 4 -> Mostrar tabela de livros; \n 5 -> Para fechar o sistema.')
escolha = int(input('Digite: '))

while True:
    if escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4 or escolha == 5:
        break
    else:
        print('Número não reconhecido! Digite o número novmente!')
        print('O que você deseja fazer?  \n 1 -> Pesquisar livro pelo título; \n 2 -> Cadastrar novos livros; \n 3 -> Deletar livro; \n 4 -> Mostrar tabela de livros.')
        escolha = int(input('Digite: '))

while True:
    if escolha == 1:
        Pesquisar()
        print('O que você deseja fazer?  \n 1 -> Pesquisar livro pelo título; \n 2 -> Cadastrar novos livros; \n 3 -> Deletar livro; \n 4 -> Mostrar tabela de livros; \n 5 -> Para fechar o sistema.')
        escolha = int(input('Digite: '))
    elif escolha == 2:
        cadastro()
        print('O que você deseja fazer?  \n 1 -> Pesquisar livro pelo título; \n 2 -> Cadastrar novos livros; \n 3 -> Deletar livro; \n 4 -> Mostrar tabela de livros; \n 5 -> Para fechar o sistema.')
        escolha = int(input('Digite: '))
    elif escolha == 3:
        excluir_livros()
        print('O que você deseja fazer?  \n 1 -> Pesquisar livro pelo título; \n 2 -> Cadastrar novos livros; \n 3 -> Deletar livro; \n 4 -> Mostrar tabela de livros; \n 5 -> Para fechar o sistema.')
        escolha = int(input('Digite: '))
    elif escolha == 4:
        mostrar()
        print('O que você deseja fazer?  \n 1 -> Pesquisar livro pelo título; \n 2 -> Cadastrar novos livros; \n 3 -> Deletar livro; \n 4 -> Mostrar tabela de livros; \n 5 -> Para fechar o sistema.')
        escolha = int(input('Digite: '))
    elif escolha == 5:
        break

print('Sistema Finalizado!')















