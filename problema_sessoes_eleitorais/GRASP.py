import random
import time

from Instancia import *

class Grasp:
    Instancia.carregar_instancia()

    # Instance
    J = Instancia.J
    K = Instancia.K
    I = Instancia.I
    e = Instancia.e
    d = Instancia.d
    M = Instancia.M
    S = Instancia.S
    iTG = 100 #Iterações Grasp
    tTG = 300 #Tempo Grasp
    iTL = 30 #Iterações Local Search
    @classmethod
    def todos_atendidos(self, Y):
        for i in Y:
            if i == None:
              return True
        return False
    @classmethod
    def construction(cls):
        cls.X = [0] * cls.J
        cls.Y = [None] * cls.I

        while cls.todos_atendidos(cls.Y):
          Jcandidatos = [(0, 0)] * round(cls.J * 0.75)
          for j in range(0, cls.J):
            if cls.K[j] > min(Jcandidatos, key=lambda x: x[1])[1] and cls.X[j] == 0:
             index = Jcandidatos.index(min(Jcandidatos, key=lambda x: x[1]))
             Jcandidatos[index] = [j, cls.K[j]]
          Jescolhido = random.choice([t[0] for t in Jcandidatos])
          dem_alocada = Grasp.calcDemandaAlocada()
          capAtual = (cls.K[Jescolhido] - dem_alocada[Jescolhido])
          cls.X[Jescolhido] = 1
          while capAtual > 0:
              for i in range(0, len(cls.e)):
                if (cls.e[i] <= capAtual) and (cls.d[i][Jescolhido] < cls.d[i][cls.Y[i]] if not cls.Y[i] == None else 99999): #and cls.Y == None
                    cls.Y[i] = Jescolhido
                    dem_alocada = Grasp.calcDemandaAlocada()
                    capAtual = cls.K[Jescolhido] - dem_alocada[Jescolhido]
              capAtual = 0
        print('Criacao')
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
        return dem_alocada

    @classmethod
    def localSearch(cls, S_inicial_X, S_inicial_Y):
       i = 0
       controlSearchLoop = 0
       while i <= cls.iTL:
        if not((i >= 1) and (controlSearchLoop == 0)):
            i += 1
            dem_alocada = Grasp.calcDemandaAlocada()
            for j in range(len(dem_alocada)):
                for k in range(len(dem_alocada)):
                    dem_alocada = Grasp.calcDemandaAlocada()
                    if ((dem_alocada[j] + dem_alocada[k]) < cls.K[j]) and (S_inicial_X[j] == 1) and (cls.X[k] == 1) and (j != k):
                        controlSearchLoop = 1
                        S_inicial_X[k] = 0
                        print(k, 'Desalocado')
                        for t in range(len(S_inicial_Y)):
                            if S_inicial_Y[t] == k:
                                S_inicial_Y[t] = j

        else:
            i = cls.iTL + 1
       print('LocalSearch Return')
       print(S_inicial_X)
       print(S_inicial_Y)
       return S_inicial_X, S_inicial_Y

    @classmethod
    def execGrasp(cls):
        inicio = time.time()
        i = 1
        Grasp.construction()
        S_inicial_X, S_inicial_Y = cls.X, cls.Y
        S_final_X, S_final_Y = cls.X, cls.Y
        while cls.iTG and i < cls.iTG:
           print('Iteracao', i)
           result_localSearch = Grasp.localSearch(S_inicial_X, S_inicial_Y)
           S_inicial_X = result_localSearch[0]
           S_inicial_Y = result_localSearch[1]


           value_fo_inicial = sum(cls.M * S_inicial_X[j] for j in range(cls.J)) + sum([cls.e[i] * cls.d[i][j] *
                                                                         (1 if S_inicial_Y[i] == j else 0)for i in range(cls.I) for j in range(cls.J)])

           value_fo_final = sum(cls.M * S_final_X[j] for j in range(cls.J)) + sum([cls.e[i] * cls.d[i][j] *
                                                                         (1 if S_final_Y[i] == j else 0)for i in range(cls.I) for j in range(cls.J)])

           print('Value F0 Inicial', value_fo_inicial)
           print('Value FO Final', value_fo_final)

           if value_fo_inicial < value_fo_final:
             if value_fo_inicial < 144568924.8241849:
              print('0')

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
        fim = time.time()
        print('Tempo', fim - inicio)

Grasp.execGrasp()
