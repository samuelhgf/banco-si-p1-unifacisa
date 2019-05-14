class Banco :

    def __init__(self) :
        self.clientes = []
        self.conta_atual = 0
        self.cria_conta('Teste', '4183419847', '1234')
        
    def exibe_menu(self) :
        print('Bem-vindo ao banco de SI\n')
        print('1. Listar clientes\n2. Criar cliente\n3. Remover cliente\n4. Editar cliente\n5. Fazer deposito\n6. Fazer saque\n7. Fazer transferencia\n8. Saldo de Conta\n9. Extrato de conta')
        opcao = int(raw_input('\nDigite uma opcao: '))
        while opcao < 1 or opcao > 9 :
            print('ERRO: OPCAO INVALIDA')
            opcao = int(raw_input('Digite uma opcao: '))
        return opcao

    def extrato(self, cpf, senha) :
        pass

    def saldo(self, cpf, senha) :
        pass
    
    def faz_transferencia(self, cpf_origem, senha_origem, cpf_destino, valor) :
        pass

    def faz_saque(self, cpf, senha, valor) :
        pass

    def faz_deposito(self, cpf, valor) :
        pass

    def edita_cliente(self, cpf, senha_atual, novo_nome, nova_senha) :
        pass
    
    def remove_cliente(self, cpf, senha) :
        pass

    def existe_cliente(self, cpf) :
        for cliente in self.clientes :
            if cliente.cpf == cpf :
                return True
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
        
    def __str__(self) :
        return 'NOME: ' + self.nome + '\nCPF: ' + self.cpf + '\nSENHA: *****' + '\nAGENCIA: ' + str(self.agencia) + '\nCONTA: ' + str(self.conta) + '\nSALDO: ' + str(self.saldo)
