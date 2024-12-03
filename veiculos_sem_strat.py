class Veiculo:
    def __init__(self, nome):
        self.nome = nome

    def mover(self, tipo_movimento):
        if tipo_movimento == "voar":
            return f"{self.nome} está voando!"
        elif tipo_movimento == "dirigir":
            return f"{self.nome} está dirigindo!"
        elif tipo_movimento == "navegar":
            return f"{self.nome} está navegando!"
        else:
            return f"{self.nome} não pode se mover desse jeito!"

carro = Veiculo("Carro")
print(carro.mover("dirigir"))

barco = Veiculo("Barco")
print(barco.mover("navegar"))

aviao = Veiculo("Avião")
print(aviao.mover("voar"))
