import datetime

class Cliente:
    def __init__(self,cpf,nome,endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        Banco(self.nome, self.cpf)

class Extrato:
    def __init__(self):
        self.transacoes = []


    def extrato(self, numeroconta):
        print(f'Extrato : {numeroconta} \n')
        for p in self.transacoes:
            print(f'{p[0]:15s}{p[1]:10.2f}{p[2]:10s} {p[3].strftime("%d/%b/%y")}')


class Conta:
    def __init__(self,clientes,numero,saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.date.today()
        self.extrato = Extrato() 

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.date.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.date.today()]) 
            return True

    def transfereValor(self, contadestino, valor):
        if self.saldo < valor:
            return print("Não existe saldo suficiente")
        else:
            contadestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.date.today()]) 
            return print("Transferencia Realizada")

    def gerarsaldo(self):
        print(f"numero: {self.numero}\n saldo:{self.saldo}")


class Banco(Cliente):
    def __init__(self, clientes, contas):
        self.clientes = clientes
        self.contas = contas
        numeros_contas = []
        numeros_contas.append(self.contas)
        tot_clientes = []
        tot_clientes.append(self.clientes)
    def monstrar_clientes(self, tot_clientes, numeros_contas):
        print(tot_clientes, numeros_contas)


cliente1 = Cliente("123","Joao","Rua X")
cliente2 = Cliente ("456","Maria","Rua W")
cliente3 = Cliente('234', 'Lucas', 'Rua a')
conta1 = Conta([cliente1,cliente2],1,2000)
conta1.depositar(1000)
conta1.sacar(1500)
conta2 = Conta([cliente3, cliente2], 3, 3000)
conta2.depositar(2000)
conta2.transfereValor(conta1, 200)
conta2.extrato.extrato(conta2.numero)
conta1.extrato.extrato(conta1.numero)
conta1.gerarsaldo(), conta2.gerarsaldo()
Banco.monstrar_clientes()
