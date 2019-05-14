from datetime import datetime
class Banco :

    def __init__(self) :
        self.clientes = []
        self.conta_atual = 0
        self.cria_conta('Samuel', '05218863335', 1234)
        
        
    def exibe_menu(self) :
        print('Bem-vindo ao banco de SI\n')
        print('1. Listar clientes\n2. Criar cliente\n3. Remover cliente\n4. Editar cliente\n5. Fazer deposito\n6. Fazer saque\n7. Fazer transferencia\n8. Saldo de Conta\n9. Extrato de conta')
        opcao = int(input('\nDigite uma opcao: '))
        while opcao < 1 or opcao > 9 :
            print('ERRO: OPCAO INVALIDA')
            opcao = int(input('Digite uma opcao: '))
        return opcao

    def extrato(self, cpf, senha) :
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                if cliente.senha == senha:
                    print('\n---------------EXTRATO BANCARIO DE ' + cliente.nome.upper() + '---------------\n')
                    for operacao in cliente.extrato:
                        print(operacao + '\n')

                    print(datetime.now().strftime('%d/%m/%Y %H:%M') + ' / Saldo atual / R$' + str(cliente.saldo))    
                else:
                    return print('Senha incorreta')

    def saldo(self, cpf, senha) :
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                if cliente.senha == senha:
                    return print('\nSeu saldo em conta é: R$ ' + str(cliente.saldo) + '\n')
                else:
                    return print('Senha incorreta')
    def faz_transferencia(self, cpf_origem, senha_origem, cpf_destino, valor) :
        for cliente in self.clientes:
            if cliente.cpf == cpf_origem:
                if cliente.senha == senha_origem:
                    if self.tem_saldo(cliente.cpf, valor):
                        cliente.saldo -= valor
                        cliente.extrato.append(datetime.now().strftime('%d/%m/%Y %H:%M') + ' / Transferencia online: ' + cpf_destino + ' / D R$' + str(valor))
                        for cliente2 in self.clientes:
                            if cliente2.cpf == cpf_destino:
                                cliente2.saldo += valor
                                cliente2.extrato.append(datetime.now().strftime('%d/%m/%Y %H:%M') + ' / Transferencia online: ' + cpf_origem + ' / C R$' + str(valor))
                                return print('Transferencia realizada com sucesso!')
                else:
                    return print('Senha incorreta')
    def faz_saque(self, cpf, senha, valor) :
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                if cliente.senha == senha:
                    if self.tem_saldo(cpf, valor):
                        cliente.saldo -= valor
                        cliente.extrato.append(datetime.now().strftime('%d/%m/%Y %H:%M') + ' / Saque em caixa eletronico / D R$' + str(valor))
                        return print('Saque ralizado com sucesso!')
                else:
                    return print('Senha incorreta')
    def faz_deposito(self, cpf, valor) :
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                cliente.saldo += valor
                cliente.extrato.append(datetime.now().strftime('%d/%m/%Y %H:%M') + ' / Deposito online / C R$' + str(valor))
                print('Deposito realizado com sucesso!')
    def edita_cliente(self, cpf, senha_atual, novo_nome, nova_senha) :
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                if cliente.senha == senha_atual:
                    cliente.nome = novo_nome
                    cliente.senha = nova_senha
                    return print('Dados alterados com sucesso!')
                else:
                    return print('Senha incorreta')
    
    def remove_cliente(self, cpf, senha) :
        for cliente in self.clientes :
            if cliente.cpf == cpf:
                if cliente.senha == senha:
                    self.clientes.remove(cliente)
                    return print('Cliente removido com sucesso')
                else:
                    return print('Senha incorreta')

    def existe_cliente(self, cpf) :
        for cliente in self.clientes :
            if cliente.cpf == cpf :
                return True
        return False

    def tem_saldo(self, cpf, valor_saida):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                if valor_saida <= cliente.saldo:
                    return True
                else:
                    print('Saldo insuficiente')
                    return False

    def lista_clientes(self) :
        print('\nLISTA DE CLIENTES ATUAL: \n')
        for cliente in self.clientes :
            print(cliente)
            print('')
        print('')
            
    def cria_conta(self, nome, cpf, senha) :
        if not self.existe_cliente(cpf) :
            cliente = Cliente(nome, cpf, senha)
            cliente.agencia = 1

            self.conta_atual += 1
            cliente.conta = self.conta_atual

            cliente.saldo = 0
            self.clientes.append(cliente)
            print('\n.: CLIENTE CADASTRADO COM SUCESSO\n')
        else :
            print('ERRO: CPF JA CADASTRADO')



# ---------------------------------------------- #
class Cliente :

    def __init__(self, nome, cpf, senha) :
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.agencia = None
        self.conta = None
        self.saldo = None
        self.extrato = []
        
    def __str__(self) :
        return 'NOME: ' + self.nome + '\nCPF: ' + self.cpf + '\nSENHA: *****' + '\nAGENCIA: ' + str(self.agencia) + '\nCONTA: ' + str(self.conta) + '\nSALDO: ' + str(self.saldo)
