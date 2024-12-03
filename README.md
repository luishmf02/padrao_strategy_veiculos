# Padrão Strategy

Trabalho Engenharia de Software II

---

## 1. Comparação entre Código com e sem Strategy

### Código **Sem Strategy**

O código sem Strategy utiliza uma lógica condicional para lidar com diferentes tipos de comportamentos (`voar`, `dirigir`, `navegar`). Embora funcional, essa abordagem apresenta problemas, como:
- O método que controla os comportamentos (no caso, `mover`) cresce à medida que novos tipos de movimento são adicionados.
- Viola o princípio de **abertura e fechamento (OCP)**, já que qualquer mudança nos tipos de movimento exige alterações diretas na classe principal.
- Torna o código menos modular e mais difícil de testar.

#### Exemplo:
```python
class Veiculo:
    def mover(self, tipo_movimento):
        if tipo_movimento == "voar":
            return "Voando!"
        elif tipo_movimento == "dirigir":
            return "Dirigindo!"
        elif tipo_movimento == "navegar":
            return "Navegando!"
        else:
            return "Movimento não reconhecido!"

### Código **Com Strategy**
Com o padrão Strategy, cada comportamento (voar, dirigir, navegar) é encapsulado em uma classe específica. Isso permite:

- Adicionar novos comportamentos sem alterar a classe principal (VeiculoComStrategy).
- Trocar o comportamento dinamicamente, sem modificar o código existente.
- Melhorar a modularidade e a testabilidade, já que cada estratégia é independente.

class Voar(EstrategiaMovimento):
    def mover(self, nome):
        return f"{nome} está voando!"

class VeiculoComStrategy:
    def __init__(self, nome, estrategia_movimento):
        self.estrategia_movimento = estrategia_movimento

O padrão Strategy separa responsabilidades, promove reutilização e evita a necessidade de alterações repetitivas em classes existentes, algo que é problemático na abordagem sem Strategy.


## 2. Identificação de Refatorações que Aplicam o Padrão Strategy

O padrão Strategy é uma ótima escolha para cenários onde:

Código possui muitas estruturas condicionais: No exemplo inicial, o método mover cresce de forma descontrolada com cada novo tipo de movimento. Refatorar utilizando Strategy resolve isso ao delegar o comportamento para classes específicas.

Comportamentos podem mudar em tempo de execução: Com Strategy, é fácil trocar a estratégia em uso sem alterar a implementação base, como demonstrado ao fazer o Carro "voar".

Reaproveitamento de lógica em múltiplas classes: Se várias classes precisassem de lógicas similares (como voar ou dirigir), as estratégias poderiam ser reutilizadas sem duplicação de código.

## 3. Pontos Fortes e Fracos do Padrão Strategy


Pontos Fortes:

Modularidade: Cada comportamento é encapsulado em uma classe separada, facilitando a manutenção.
Extensibilidade: Adicionar novos comportamentos não requer alterações na classe principal.
Testabilidade: Cada estratégia pode ser testada de forma independente.
Flexibilidade: Comportamentos podem ser alterados em tempo de execução.

Pontos Fracos:

Aumento do número de classes: Para cada novo comportamento, uma nova classe deve ser criada.
Overhead inicial: Em problemas simples, o uso de Strategy pode parecer excessivo.
Dificuldade para novos desenvolvedores: Quem não está familiarizado com o padrão pode achar a separação de responsabilidades mais difícil de entender no início.

## 4. Conclusões Finais

O padrão Strategy é ideal para cenários onde comportamentos variam ou podem ser trocados dinamicamente. Ele:

Promove o uso de boas práticas, como o princípio de responsabilidade única (SRP) e abertura e fechamento (OCP).
Facilita a manutenção e expansão de sistemas complexos.
Entretanto, deve ser utilizado com parcimônia em problemas muito simples, para evitar introdução desnecessária de complexidade.
No caso deste exemplo, o padrão foi fundamental para transformar uma lógica baseada em if/elif em uma solução modular e escalável. Em aplicações reais, é frequentemente usado em jogos, sistemas de autenticação, motores de recomendação e outras áreas que exigem flexibilidade no comportamento.

