from abc import ABC, abstractmethod

# Estratégia base
class EstrategiaMovimento(ABC):
    @abstractmethod
    def mover(self, nome):
        pass

# Estratégias concretas
class Voar(EstrategiaMovimento):
    def mover(self, nome):
        return f"{nome} está voando!"

class Dirigir(EstrategiaMovimento):
    def mover(self, nome):
        return f"{nome} está dirigindo!"

class Navegar(EstrategiaMovimento):
    def mover(self, nome):
        return f"{nome} está navegando!"

# Classe Veículo usando Strategy
class VeiculoComStrategy:
    def __init__(self, nome, estrategia_movimento):
        self.nome = nome
        self.estrategia_movimento = estrategia_movimento

    def mover(self):
        return self.estrategia_movimento.mover(self.nome)

# Testes
if __name__ == "__main__":
    carro = VeiculoComStrategy("Carro", Dirigir())
    print(carro.mover())

    barco = VeiculoComStrategy("Barco", Navegar())
    print(barco.mover())

    aviao = VeiculoComStrategy("Avião", Voar())
    print(aviao.mover())

    # Alterando comportamento dinamicamente
    carro.estrategia_movimento = Voar()
    print(f"Agora o {carro.nome}: {carro.mover()}")
