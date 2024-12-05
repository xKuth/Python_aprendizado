'''from datetime import date
class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    @classmethod
    def apartirAnoNacimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)
    @staticmethod
    def EhmaiorIdade(idade):
        return idade >= 18
pessoa1 = pessoa('maria', 26)
pessoa2 = pessoa.apartirAnoNacimento('ana', 2006)
print(pessoa1.idade)
print(pessoa2.idade)
print(pessoa.EhmaiorIdade(17))
        '''


class Cliente:
    def __init__(self,cpf,nome,endereco):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
    

class Conta(Cliente):
    def __init__(self, clientes, numero, saldo, nome, endereco):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.endereco = endereco
        print(self.nome, self.endereco)
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self,valor):
      if self.saldo < valor:
         return False
      else:
         self.saldo -= valor
         return True
    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
            self.contadestino = contaDestino
            self.saldo -= valor
            return("Transferencia Realizada")
    def gerarsaldo(self):
        print(f'numero:{self.numero} \nsaldo: {self.saldo}')

cliente1 = Cliente(123, 'Joao', 'Rua 1')
cliente2 = Cliente(345, 'Maria','Rua 2')
cliente3 = Cliente(234, 'João', 'rua A')
cliente4 = Cliente(564, 'Mateus', 'Rua B')
p_conta = Conta(cliente1.cpf, 234, 500, [cliente1.nome, cliente2.nome, cliente3.nome, cliente4.nome], [cliente1.endereco, cliente2.endereco,
                                                                                                       cliente3.endereco, cliente4.endereco])