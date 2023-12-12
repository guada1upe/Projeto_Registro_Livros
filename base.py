import mysql.connector

conectar = mysql.connector.connect(host ='localhost', database = 'Sistema_Registro_Livros', user='root', password = 'teste@123')

print('Bem-vindo a nossa biblioteca!')

print('O que você deseja fazer?  \n 1 -> Pesquisar livro pelo título; \n 2 -> Cadastrar novos livros; \n 3 -> Deletar livro; \n 4 -> Mostrar tabela de livros.')
escolha = int(input('Digite: '))

