import json
from banco import *

def cpf_cadastrado(cpf):
    while len(cpf) != 11 or not banco.existe_cliente(cpf):
        cpf = input('Cpf invalido, digite novamente: ')
    return cpf

def cpf_valido(cpf):
    while len(cpf) != 11:
        cpf = input('Cpf invalido, digite novamente: ')
    return cpf

def pede_dados_cliente() :
    nome = input('Digite o nome: ')
    cpf = cpf_valido(input('Digite o cpf: '))
    senha = int(input('Digite a senha de acesso: '))
    return nome, cpf, senha

def pede_dados_remocao():
    cpf = cpf_cadastrado(input('Digite o cpf: '))
    senha = int(input('Digite a senha: '))
    return cpf, senha

def pede_dados_edicao():
    cpf = cpf_cadastrado(input('Digite o cpf: '))
    senha_atual = int(input('Digite a senha atual: '))
    novo_nome = input('Digite o novo nome: ')
    nova_senha = int(input('Digite a nova senha: '))
    return cpf, senha_atual, novo_nome, nova_senha

def pede_dados_deposito():
    cpf = cpf_cadastrado(input('Digite o cpf da conta de destino: '))
    valor = int(input('Digite o valor (Nao aceitamos moedas): '))
    return cpf, valor

def pede_dados_saque():
    cpf = cpf_cadastrado(input('Digite o cpf: '))
    senha = int(input('Digite a senha: '))
    valor = int(input('Digite o valor (Nao aceitamos moedas): '))
    return cpf, senha, valor

def pede_dados_transferencia():
    cpf_origem = cpf_cadastrado(input('Digite o cpf da conta de origem: '))
    senha_origem = int(input('Digite a senha da conta de origem: '))
    cpf_destino = cpf_cadastrado(input('Digite o cpf da conta de destino: '))
    valor = int(input('Digite o valor :'))
    return cpf_origem, senha_origem, cpf_destino, valor

def pede_dados_saldo_extrato():
    cpf = cpf_cadastrado(input('Digite o cpf: '))
    senha = int(input('Digite a senha: '))
    return cpf, senha

continuar = 's'
banco = Banco()
while continuar.lower() == 's' :
    opcao = banco.exibe_menu()
    if opcao == 1 :
        banco.lista_clientes()  
    elif opcao == 2 :
        nome, cpf, senha = pede_dados_cliente()
        banco.cria_conta(nome, cpf, senha)
    elif opcao == 3:
        cpf, senha = pede_dados_remocao()
        banco.remove_cliente(cpf, senha)
    elif opcao == 4:
        cpf, senha_atual, novo_nome, nova_senha = pede_dados_edicao()
        banco.edita_cliente(cpf, senha_atual, novo_nome, nova_senha)
    elif opcao == 5:
        cpf, valor = pede_dados_deposito()
        banco.faz_deposito(cpf, valor)
    elif opcao == 6:
        cpf, senha, valor = pede_dados_saque()
        banco.faz_saque(cpf, senha, valor)
    elif opcao == 7:
        cpf_origem, senha_origem, cpf_destino, valor = pede_dados_transferencia()
        banco.faz_transferencia(cpf_origem, senha_origem, cpf_destino, valor)
    elif opcao == 8:
        cpf, senha = pede_dados_saldo_extrato()
        banco.saldo(cpf, senha)
    elif opcao == 9:
        cpf, senha = pede_dados_saldo_extrato()
        banco.extrato(cpf, senha)
        
        
    
    continuar = input('Deseja continuar (s/n): ')


print('Au revoir!')
