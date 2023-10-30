import math


class Distancias:
    def calc_distancias(n, setores):
        distancias = {}
        for i in range(n):
            for j in range(n):
                ponto1 = setores['chave' + str(i + 1)]['valor']
                ponto2 = setores['chave' + str(j + 1)]['valor']
                if ponto1 == ponto2:
                    distancia = 0
                    chave = 'chave' + str(i + 1) + ',' + str(j + 1)
                    distancias[chave] = distancia
                else:
                        x1, y1 = ponto1
                        x2, y2 = ponto2
                        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                        chave = 'chave' + str(i + 1) + ',' + str(j + 1)
                        distancias[chave] = distancia
        return distancias

    def retorna_dist_necessarias(distancias, n, locais):
        matriz_dist = [[0 for _ in range(len(locais))] for _ in range(n)]
        teste = 0
        for i in range(n):
         chaveLocais = 'chave' + str(i + 1)
         if chaveLocais in locais:
            teste += 1
            for j in range(n):
                 chave = 'chave' + str(i + 1) + ',' + str(j + 1)
                 matriz_dist[j][teste - 1] = distancias[chave]
        return matriz_dist



