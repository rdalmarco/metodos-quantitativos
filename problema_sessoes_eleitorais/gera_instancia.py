from Distancias import *
from Setores import *
from Locais import *

num_set = 25
lado = 1000
num_locais = 5
cap_atendi_total = 70000
demanda_setores_total = 35000
porcent_pop_urbana = 0.76
porcent_pop_rural = 0.24
dic_setores = {}
pos_central = []
distancias = {}
class_setores = {}
locais = []


def gera_instancia(num_set, lado):
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


    J = num_locais;
    E = num_set;

    K = [0] * num_locais
    kindex = 0
    for i in range(num_set):
        chave = 'chave' + str(i + 1)
        if chave in locais:
          K[kindex] = locais[chave]['valor']
          kindex += 1

    e = [0] * num_set
    eindex = 0
    for i in range(num_set):
        chave = 'chave' + str(i + 1)
        if chave in class_setores:
          e[eindex] = class_setores[chave]['demanda']
          eindex += 1

    d = Distancias.retorna_dist_necessarias(distancias, num_set, locais)

    print(J)
    print(E)
    print(K)
    print(e)
    print(d)


gera_instancia(num_set, lado)
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


