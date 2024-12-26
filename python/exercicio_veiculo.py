class Veiculo:


    def __init__(self, nome, vel_max, km_litro):
        self.nome = nome
        self.vel_max = vel_max
        self.km_litro = km_litro

    def capacidade_assentos(self, capacidade):
        print(f'a capacidade maxima de assentos do {self.nome} é de {capacidade}')


    def imprimir(self):
        print(f'O veiculo: {self.nome}')
        print(f'velocidade maxima: {self.vel_max}')
        print(f'km litro: {self.km_litro}')

class onibus(Veiculo):
    def capacidade_assentos(self, capacidade=70):
        return super().capacidade_assentos(capacidade=70)

# carro1 = Veiculo('punto', 200, 14)
# carro1.imprimir()
onibus_escolar = onibus('Scania', 150, 4)
onibus_escolar.imprimir()
onibus_escolar.capacidade_assentos()