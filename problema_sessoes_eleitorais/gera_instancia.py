from Distancias import *
from Setores import *
from Locais import *

num_set = 25
lado = 1000
num_locais = 5
dic_setores = {}
pos_central = []
m_distancias = [[]]
class_setores = {}
locais = []


def gera_instancia(num_set, lado):
    global pos_central
    global dic_setores
    global m_distancias
    global class_setores
    global locais

    pos_central = Setores.calc_pos_central(lado)
    dic_setores = Setores.calcular_centros_setores(num_set, lado)
    m_distancias = Distancias.calc_distancias(num_set, dic_setores)
    class_setores = Setores.class_setor(pos_central, dic_setores)
    locais = Locais.gera_locais(class_setores, num_locais)


gera_instancia(num_set, lado)
print(dic_setores)
print(pos_central)
print(m_distancias)
print(class_setores)
print(locais)


