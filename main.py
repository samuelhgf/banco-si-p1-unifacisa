from banco import *

def pede_dados_cliente() :
    nome = input('Digite o nome: ')
    cpf = input('Digite o cpf: ')
    senha = input('Digite a senha de acesso: ')
    return nome, cpf, senha



continuar = 's'
banco = Banco()
while continuar.lower() == 's' :
    opcao = banco.exibe_menu()
    if opcao == 1 :
        banco.lista_clientes()  
    elif opcao == 2 :
        nome, cpf, senha = pede_dados_cliente()
        banco.cria_conta(nome, cpf, senha)    
    
    continuar = input('Deseja continuar (s/n): ')

print('Au revoir!')
