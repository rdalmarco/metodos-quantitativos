from calc_centros import calc_centros
from calc_distancias import calc_distancias

n = 25;
L = 1000;
def gera_instancia(n, L):
    pos_central = calc_centros.calc_pos_central(L)
    centros = calc_centros.calcular_centros_setores(n, L)
    distancias = calc_distancias.calc_distancias(n, centros)

gera_instancia(n, L)
