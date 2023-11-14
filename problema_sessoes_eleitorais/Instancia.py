import json

from Distancias import *
from Setores import *
from Locais import *

num_set = 400
lado = 20000
num_locais = 25
cap_atendi_total = 700000
demanda_setores_total = 200000
porcent_pop_urbana = 1.24
porcent_pop_rural = 0.76
dic_setores = {}
pos_central = []
distancias = {}
class_setores = {}
locais = []

class Instancia:
    J = 0
    K = 0
    I = num_set
    e = []
    d = [[]]
    S = 100000
    M = 0

    @classmethod
    def gera_instancia(cls): #cls, num_set, lado
        global pos_central
        global dic_setores
        global distancias
        global class_setores
        global locais
        global cap_atendi_total

        pos_central = Setores.calc_pos_central(lado)
        dic_setores = Setores.calcular_centros_setores(num_set, lado)
        distancias = Distancias.calc_distancias(num_set, dic_setores)
        class_setores = Setores.class_setor(pos_central, dic_setores, demanda_setores_total, num_set, porcent_pop_urbana, porcent_pop_rural)
        locais = Locais.gera_locais(class_setores, num_locais, cap_atendi_total)

        cls.J = num_locais
        cls.I = num_set

        cls.K = [0] * num_locais
        kindex = 0
        for i in range(num_set):
            chave = 'chave' + str(i + 1)
            if chave in locais:
                cls.K[kindex] = locais[chave]['valor']
                kindex += 1

        cls.e = [0] * num_set
        eindex = 0
        for i in range(num_set):
            chave = 'chave' + str(i + 1)
            if chave in class_setores:
                cls.e[eindex] = class_setores[chave]['demanda']
                eindex += 1

        cls.d = Distancias.retorna_dist_necessarias(distancias, num_set, locais)

        cls.M = max(cls.e) * max([max(row) for row in cls.d]) * cls.J

        print(cls.J)
        print(cls.I)
        print(cls.K)
        print(cls.e)
        print(cls.d)
        Instancia.salvar_instancia()

    @classmethod
    def get_J(cls):
        return cls.J

    @classmethod
    def get_K(cls):
        return cls.K

    @classmethod
    def get_I(cls):
        return cls.I

    @classmethod
    def get_e(cls):
        return cls.e

    @classmethod
    def get_d(cls):
        return cls.d

    @classmethod
    def get_M(cls):
        return cls.M

    @classmethod
    def get_S(cls):
        return cls.S

    @classmethod
    def salvar_instancia(cls):
        instancia = {
            'J': cls.J,
            'K': cls.K,
            'I': cls.I,
            'e': cls.e,
            'd': cls.d,
            'M': cls.M,
            'S': cls.S
        }

        with open('instancia.json', 'w') as file:
            json.dump(instancia, file)

    @classmethod
    def carregar_instancia(cls):
        with open('instancia.json', 'r') as file:
            instancia = json.load(file)

        cls.J = instancia['J']
        cls.K = instancia['K']
        cls.I = instancia['I']
        cls.e = instancia['e']
        cls.d = instancia['d']
        cls.M = instancia['M']
        cls.S = instancia['S']

#Instancia.gera_instancia(num_set, lado)
print('Centro setores')
print(dic_setores)
print('Valor posição central')
print(pos_central)
print('Distancias')
print(distancias)
print('Setores e sua classificação')
print(class_setores)
print('Locais e suas capacidades')
print(locais)
