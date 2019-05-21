from datetime import datetime
from conn import *
c_db = Conn()

class Banco :

    def __init__(self) :
        self.clientes = []
        self.conta_atual = 0

        clientes_bd = c_db.get_clients()

        extratos_bd = c_db.get_extratos()

        for i in list(clientes_bd):
            usuario = Cliente(i[0], i[1], i[2], i[3], i[4], i[5])
            self.clientes.append(usuario)


        for cliente in self.clientes:
            for extrato in list(extratos_bd):
                if cliente.cpf == extrato[0]:
                    cliente.extrato.append(extrato[4].strftime("%d/%m/%Y %H:%M") + ' / ' + extrato[1] + ' / ' + extrato[2] + ' R$' + str(extrato[3]))
        
        
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

                    print(datetime.now().strftime('%d/%m/%Y %H:%M') + ' / Saldo atual / R$' + str(cliente.saldo)+'\n')    
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
                        novo_saldo = cliente.saldo - valor
                        if c_db.altera_saldo(cliente.cpf, novo_saldo):
                            
                            cliente.saldo -= valor   

                        for cliente2 in self.clientes:
                            if cliente2.cpf == cpf_destino:
                                novo_saldo = cliente2.saldo - valor
                                if c_db.altera_saldo(cliente2.cpf, novo_saldo):

                                    c_db.add_extrato(cliente.cpf, 'Transferência online: ' + cliente2.nome, 'D', valor)

                                    cliente.extrato.append(datetime.now().strftime('%d/%m/%Y %H:%M') + ' / Transferencia online: ' + cliente2.nome + ' / D R$' + str(valor))

                                    c_db.add_extrato(cliente2.cpf, 'Transferência online: ' + cliente.nome, 'C', valor)
                                    
                                    cliente2.saldo += valor
                                    
                                    cliente2.extrato.append(datetime.now().strftime('%d/%m/%Y %H:%M') + ' / Transferencia online: ' + cliente.nome + ' / C R$' + str(valor))

                                    print('Transferencia realizada com sucesso!')
                else:
                    return print('Senha incorreta')
    def faz_saque(self, cpf, senha, valor) :
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                if cliente.senha == senha:
                    if self.tem_saldo(cpf, valor):
                        novo_saldo = cliente.saldo - valor

                        if c_db.altera_saldo(cpf, novo_saldo):
                            cliente.saldo = novo_saldo

                            c_db.add_extrato(cpf, 'Saque em caixa eletrônico', 'D', valor)

                            cliente.extrato.append(datetime.now().strftime('%d/%m/%Y %H:%M') + ' / Saque em caixa eletrônico / D R$' + str(valor))

                            print('Saque realizado com sucesso')
                        else:
                            print('Saque não realizado')
                else:
                    return print('Senha incorreta')
    def faz_deposito(self, cpf, valor) :
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                saldo = cliente.saldo
                novo_saldo = cliente.saldo + valor
                if c_db.altera_saldo(cpf, novo_saldo):
                    c_db.add_extrato(cpf, 'Deposito online', 'C', valor)

                    cliente.saldo += valor

                    cliente.extrato.append(datetime.now().strftime('%d/%m/%Y %H:%M') + ' / Deposito online / C R$' + str(valor))
                else:
                    print('Deposito nao realizado')
    def edita_cliente(self, cpf, senha_atual, novo_nome, nova_senha) :
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                if cliente.senha == senha_atual:
                    if c_db.edita_cliente(cpf, novo_nome, nova_senha):
        
                        cliente.nome = novo_nome

                        cliente.senha = nova_senha

                        print('Dados alterados com sucesso!')

                    else:
                        print('Dados não alterados')
                else:
                    return print('Senha incorreta')
    
    def remove_cliente(self, cpf, senha) :
        for cliente in self.clientes :
            if cliente.cpf == cpf:
                if cliente.senha == senha:
                    if c_db.remove_cliente(cpf):  
                        self.clientes.remove(cliente)
                        print('Cliente removido com sucesso')
                    else:
                        print('Cliente nao removido')
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
            with c_db.con.cursor() as cursor:
                sql = "SELECT cpf FROM usuarios WHERE cpf = %s"
                cursor.execute(sql, (cpf))
                result = cursor.fetchone()
            if result:
                print('ERRO: CPF JA CADASTRADO')
            else:
                self.conta_atual += 1

                cliente = Cliente(nome, cpf, senha, 1, self.conta_atual, 0)

                self.clientes.append(cliente)
                try:
                    with c_db.con.cursor() as cursor:

                        sql = "INSERT INTO usuarios (nome, cpf, senha, agencia, conta, saldo) VALUES (%s, %s, %s, %s, %s, %s)"
                        cursor.execute(sql, (nome, cpf, senha, 1, self.conta_atual, 0))

                    c_db.con.commit()

                except:
                    print('Cliente não cadastrado')

                print('\n.: CLIENTE CADASTRADO COM SUCESSO\n')
        else :
            print('ERRO: CPF JA CADASTRADO')



# ---------------------------------------------- #
class Cliente :

    def __init__(self, nome, cpf, senha, agencia, conta, saldo) :
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.extrato = []
        
    def __str__(self) :
        return 'NOME: ' + self.nome + '\nCPF: ' + self.cpf + '\nSENHA: *****' + '\nAGENCIA: ' + str(self.agencia) + '\nCONTA: ' + str(self.conta) + '\nSALDO: ' + str(self.saldo)
