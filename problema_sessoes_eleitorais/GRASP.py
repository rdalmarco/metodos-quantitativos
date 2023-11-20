import random

from Instancia import *

class Grasp:
    """ I = 25  # Setores
    J = 5   # Locais
    K = [600, 900, 2600, 1050, 450]  # Capacidade locais
    e = [200, 100, 100, 100, 100, 200, 300, 600, 200, 350, 500, 140, 120, 110, 50, 60, 90, 10, 17, 21, 100, 230, 90, 20, 10] #Demanda setores
    d = [
        [0, 4293, 6072, 6923, 9600],
        [1920, 2715, 4293, 5431, 8587],
        [3840, 1920, 2715, 4293, 7916],
        [5760, 2715, 1920, 3840, 7680],
        [7680, 4293, 2715, 4293, 7916],
        [1920, 3840, 5760, 6072, 8146],
        [2715, 1920, 3840, 4293, 6923],
        [4293, 0, 1920, 2715, 6072],
        [6072, 1920, 0, 1920, 5760],
        [7916, 3840, 1920, 2715, 6072],
        [3840, 4293, 6072, 5760, 6923],
        [4293, 2715, 4293, 3840, 5431],
        [5431, 1920, 2715, 1920, 4293],
        [6923, 2715, 1920, 0, 3840],
        [8587, 4293, 2715, 1920, 4293],
        [5760, 5431, 6923, 6072, 6072],
        [6072, 4293, 5431, 4293, 4293],
        [6923, 3840, 4293, 2715, 2715],
        [8146, 4293, 3840, 1920, 1920],
        [9600, 5431, 4293, 2715, 2715],
        [7680, 6923, 8146, 6923, 5760],
        [7916, 6072, 6923, 5431, 3840],
        [8587, 5760, 6072, 4293, 1920],
        [9600, 6072, 5760, 3840, 0],
        [10861, 6923, 6072, 4293, 1920]
    ]
    iTG = 500
    M = 10 """

    Instancia.gera_instancia()
    #Instancia.carregar_instancia()

    # Instance
    J = Instancia.J
    K = Instancia.K
    I = Instancia.I
    e = Instancia.e
    d = Instancia.d
    M = Instancia.M
    S = Instancia.S
    iTG = 200 #Iterações Grasp
    iTL = 10 #Iterações Local Search
    @classmethod
    def todos_atendidos(self, Y):
        for i in Y:
            if i == None:
              return True
        return False
    @classmethod
    def construction(cls):
        #Solução Vazia:
        cls.X = [0] * cls.J
        cls.Y = [None] * cls.I

        #Ideia professor:
        #VetorY: Saida vetor setores atendidos [3, 3, 3, 5, 5]
        #VetorX: Saida vetor escolas instaladas [0, 0, 1, 0, 1]

        #Estrutura de grafos
        #Instala uma escola, joga as demandas dos setores nela conforme sua capacidade, quando
        #encher a capacidade dela, instala outra escola e faz a mesma coisa até acabar as demandas.

        #Função Heurística: G = Semi Gulosa
        #Será selecionado para instalação os 3 locais com maior capacidade, depois 1 deles.
        #Será selecionado para atender um setor i o local com maior capacidade mais perto dele.


        #Melhoria 1, Na construção, fazer a alocação considerando as distancias. Considera os setores próximos ao local instalado e começa a alocação por eles.
        #Melhoria 2, Na busca local, é necessário fazer uma mudança de alocação, conforme está sendo feito, e depois fazer outra em cima dessa.
        while cls.todos_atendidos(cls.Y):
          Jcandidatos = [(0, 0)] * round(cls.J * 0.90)
          for j in range(0, cls.J):
            if cls.K[j] > min(Jcandidatos, key=lambda x: x[1])[1] and cls.X[j] == 0:
             index = Jcandidatos.index(min(Jcandidatos, key=lambda x: x[1]))
             Jcandidatos[index] = [j, cls.K[j]]
          Jescolhido = random.choice([t[0] for t in Jcandidatos])
          capAtual = cls.K[Jescolhido]
          cls.X[Jescolhido] = 1
          while capAtual > 0:
              for i in range(0, len(cls.e)):
                if cls.e[i] <= capAtual and cls.Y[i] == None:
                    cls.Y[i] = Jescolhido
                    capAtual = capAtual - cls.e[i]
              capAtual = 0
        print(cls.X)
        print(cls.Y)

    @classmethod
    def calcDemandaAlocada(cls):
        dem_alocada = [0] * cls.J
        value = 0
        for j in range(len(cls.X)):
            for k in range(len(cls.Y)):
                if cls.Y[k] == j:
                    value += cls.e[k]
            dem_alocada[j] = value
            value = 0
        #print(dem_alocada)
        return dem_alocada

    @classmethod
    def localSearch(cls, S_inicial_X, S_inicial_Y):
       i = 0
       while i <= cls.iTL:
            i += 1
            dem_alocada = Grasp.calcDemandaAlocada()
            for j in range(len(dem_alocada)):
                for k in range(len(dem_alocada)):
                    dem_alocada = Grasp.calcDemandaAlocada()
                    if ((dem_alocada[j] + dem_alocada[k]) < cls.K[j]) and (S_inicial_X[j] == 1) and (cls.X[k] == 1):
                        S_inicial_X[k] = 0
                        print(k, 'Desalocado')
                        for t in range(len(S_inicial_Y)):
                            if S_inicial_Y[t] == k:
                                S_inicial_Y[t] = j
       print(S_inicial_X)
       print(S_inicial_Y)
       return S_inicial_X, S_inicial_Y

    @classmethod
    def execGrasp(cls):
        i = 1
        Grasp.construction()
        S_inicial_X, S_inicial_Y = cls.X, cls.Y
        S_final_X, S_final_Y = cls.X, cls.Y
        while i <= cls.iTG:
           print('Iteracao', i)
           result_localSearch = Grasp.localSearch(S_inicial_X, S_inicial_Y)
           S_inicial_X = result_localSearch[0]
           S_inicial_Y = result_localSearch[1]
           value_fo_inicial = sum(cls.M * S_inicial_X[j] for j in range(cls.J)) + sum([cls.e[i] * cls.d[i][j] *
                                                                         (1 if S_inicial_Y[i] == j else 0)for i in range(cls.I) for j in range(cls.J)])

           value_fo_final = sum(cls.M * S_final_X[j] for j in range(cls.J)) + sum([cls.e[i] * cls.d[i][j] *
                                                                         (1 if S_final_Y[i] == j else 0)for i in range(cls.I) for j in range(cls.J)])

           print('Value F0 Inicial',  value_fo_inicial)
           print('Value FO Final', value_fo_final)
           if value_fo_inicial < value_fo_final:
               S_final_X = S_inicial_X
               S_final_Y = S_inicial_Y
           Grasp.construction()
           S_inicial_X = cls.X
           S_inicial_Y = cls.Y
           i += 1
        print('Final Grasp', S_final_X)
        print('Final Grasp', S_final_Y)
        value_fo_good = sum(cls.M * S_final_X[j] for j in range(cls.J)) + sum([cls.e[i] * cls.d[i][j] *
                                                                                (1 if S_final_Y[i] == j else 0) for i in
                                                                                range(cls.I) for j in range(cls.J)])
        print('Fo good', value_fo_good)


          #Foca em mudar Y, conforme descrito no trabalho modelo, a ideia é ir alocando os setores
          #em locais diferentes buscando diminuir a demanda ociosa dos locais e tentando zerar algum
          #deles, dessa forma podendo tirar o mesmo da solução. Em cada busca local vou tentar
          #diminuir as demandas ociosas e tirar um local, se não for possível no número de iterações
          #retorna e se chegar a tirar um local, retorna.
          #Faz a busca local toda as vezes conforme grasp e no final calcula o valor da função objetivo
          #para pegar a melhor.

          #Basicamente, vou buscar diminuir as demandas ociosas em cada busca local fazendo
          #todas as combinações válidas de setores em locais, vou gerar todas as vizinhanças
          # mudando cada setor para cada local, mas sempre comparando se é valido a mudança
          #a ideia é sempre tentar
          #tirar um setor, diminuindo a primeira parte da função objetivo que é a mais
          #'importante'


Grasp.execGrasp()
