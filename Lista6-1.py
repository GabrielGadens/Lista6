# Você foi contratado para desenvolver um programa de simulação de batalhas medievais. Para isso, 
# você precisa implementar um sistema de unidades militares que possa se movimentar e atacar. 
# Você deve criar três classes de unidades: Soldado, Arqueiro e Cavaleiro. Todas as classes devem 
# herdar de uma classe base chamada UnidadeMilitar. A classe UnidadeMilitar deve ter os seguintes 
# métodos:
# • mover(): exibe uma mensagem indicando que a unidade está se movendo.
# • atacar(): exibe uma mensagem indicando que a unidade está atacando.
# Cada uma das classes filhas deve implementar os métodos mover() e atacar() de forma específica, 
# de acordo com a especialidade da unidade.
# Crie uma instância de cada uma das diferentes unidades (Soldado, Arqueiro e Cavaleiro), e adicione em 
# uma lista chamada unidades. Por fim, você deve percorrer o array unidades usando um loop e chamar os 
# métodos mover() e atacar() de cada unidade no array
class UnidadeMilitar:
    def __init__(self):
        print('Unidade Militar')

    def mover(self):
        print('\nmovendo-se')

    def atacar(self):
        print('\natacando')


class Soldado(UnidadeMilitar):
    def __init__(self):
        super().__init__()
        print('Novo soldado')   

    def mover(self):
        super().mover()
        print('correndo')

    def atacar(self):
        super().atacar()
        print('com espada')


class Arqueiro(UnidadeMilitar):
    def __init__(self):
        super().__init__()
        print('Novo arqueiro')

    def mover(self):
        super().mover()
        print('caminhando')

    def atacar(self):
        super().atacar()
        print('com flechas')


class Cavaleiro(UnidadeMilitar):
    def __init__(self):
        super().__init__()
        print('Novo cavaleiro')

    def mover(self):
        super().mover()
        print('a Cavalo')

    def atacar(self):
        super().atacar()
        print('com lança')

unidadesMilitar=[]
cavaleiro=Cavaleiro()
unidadesMilitar.append(cavaleiro)
soldado=Soldado()
unidadesMilitar.append(soldado)
arqueiro=Arqueiro()
unidadesMilitar.append(arqueiro)

for unid in unidadesMilitar:
    unid.mover()
    unid.atacar()
    