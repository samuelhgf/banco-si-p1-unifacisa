import pymysql.cursors
class Conn:

    def __init__(self):
        try:
            self.con = pymysql.connect(host="162.241.203.142", user="samue983_banco_u", password="123Banco", db="samue983_banco_si")
        except Exception as e:
            print(e)
            print('Erro na conexao com o banco de dados')

    def get_clients(self):
        try:
            with self.con.cursor() as cursor:
                sql = "SELECT nome, cpf, senha, agencia, conta, saldo FROM usuarios"
                cursor.execute(sql)
                return cursor
        except:
            print("Error no banco de dados")

    def add_extrato(self, cpf, msg, tipo, valor):
        try:
            with self.con.cursor() as cursor:
                sql = "INSERT INTO extratos (cpf, msg, tipo, valor) VALUES (%s, %s, %s, %s)"
                cursor.execute(sql, (cpf, msg, tipo, valor))

            self.con.commit()
        except Exception as e:
            print(e)
            print("Erro ao adiconar extrato")

    def get_extratos(self):
        try:
            with self.con.cursor() as cursor:
                sql = "SELECT cpf, msg, tipo, valor, inserido FROM extratos ORDER BY inserido ASC"
                cursor.execute(sql)
                return cursor

        except Exception as e:
            print(e)
            print("Erro no banco de dados")

    def altera_saldo(self, cpf, novo_saldo):
        try:
            with self.con.cursor() as cursor:

                sql = "UPDATE usuarios SET saldo = %s WHERE cpf = %s "
                cursor.execute(sql, (novo_saldo, cpf))

            self.con.commit()

            return True

        except Exception as e:
            print(e)
            return False

    def edita_cliente(self, cpf, novo_nome, nova_senha):
        try:
            with self.con.cursor() as cursor:

                sql = "UPDATE usuarios SET nome = %s, senha = %s WHERE cpf = %s"
                cursor.execute(sql, (novo_nome, nova_senha, cpf))

            self.con.commit()

            return True

        except Exception as e:
            print(e)
            return False

    def remove_cliente(self, cpf):
        try:
            with self.con.cursor() as cursor:

                sql = "DELETE FROM usuarios WHERE cpf = %s"
                cursor.execute(sql, (cpf))

                sql = "DELETE FROM extratos WHERE cpf = %s"
                cursor.execute(sql, (cpf))

            self.con.commit()

            return True

        except Exception as e:
            print(e)
            return False
