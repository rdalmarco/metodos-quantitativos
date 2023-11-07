import random


class Grasp:
    I = 20  # Setores
    J = 5   # Locais
    K = [600, 800, 2000, 1000, 350]  # Capacidade locais
    e = [100, 100, 100, 100, 100, 200, 300, 600, 200, 350, 500, 140, 120, 110, 50, 60, 90, 10, 17, 21] #Demanda setores

    @classmethod
    def todos_atendidos(self, Y):
        for i in Y:
            if i == 0:
              return True
        return False
    @classmethod
    def construction(cls):
        #Solução Vazia:
        cls.X = [0] * cls.J
        cls.Y = [0] * cls.I

        #Ideia professor:
        #VetorY: Saida vetor setores atendidos [3, 3, 3, 5, 5]
        #VetorX: Saida vetor escolas instaladas [0, 0, 1, 0, 1]

        #Estrutura de grafos
        #Instala uma escola, joga as demandas dos setores nela conforme sua capacidade, quando
        #encher a capacidade dela, instala outra escola e faz a mesma coisa até acabar as demandas.

        #Função Heurística: G = Semi Gulosa
        #Será selecionado para instalação os 3 locais com maior capacidade, depois 1 deles.
        #Será selecionado para atender um setor i o local com maior capacidade mais perto dele.


        while cls.todos_atendidos(cls.Y):
          capAtual = 0
          Jcandidatos = [(0, 0)] * 3
          Jescolhido = 0
          for j in range(0, cls.J):
            if cls.K[j] > min(Jcandidatos, key=lambda x: x[1])[1] and cls.X[j] == 0:
             index = Jcandidatos.index(min(Jcandidatos, key=lambda x: x[1]))
             Jcandidatos[index] = [j, cls.K[j]]
          Jescolhido = random.choice([t[0] for t in Jcandidatos])
          capAtual = cls.K[Jescolhido]
          cls.X[Jescolhido] = 1
          while capAtual > 0:
              for i in range(0, len(cls.e)):
                if cls.e[i] <= capAtual and cls.Y[i] == 0:
                    cls.Y[i] = Jescolhido
                    capAtual = capAtual - cls.e[i]
              capAtual = 0
        print(cls.X)
        print(cls.Y)

    @classmethod
    def execGrasp(cls):
        'implementar'

Grasp.construction()
