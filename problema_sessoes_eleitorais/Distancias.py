import math


class Distancias:
    def calc_distancias(n, setores):
        raizN = math.sqrt(n)
        matriz_dist = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                ponto1 = setores['chave' + str(i + 1)]['valor']
                ponto2 = setores['chave' + str(j + 1)]['valor']
                if ponto1 == ponto2:
                    distancia = 0
                    posicao1 = ((i // raizN + 1 - 1), (i % raizN + 1 - 1))
                    posicao2 = ((j // raizN + 1 - 1), (j % raizN + 1) - 1)
                    matriz_dist[j][i] = distancia
                    print(f"Distância entre Ponto {posicao1} e Ponto {posicao2}: {distancia:.2f}")
                else:
                    try:
                        posicao1 = ((i // raizN + 1 - 1), (i % raizN + 1 - 1))
                        posicao2 = ((j // raizN + 1 - 1), (j % raizN + 1) - 1)
                        x1, y1 = ponto1
                        x2, y2 = ponto2
                        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                        matriz_dist[j][i] = distancia
                    except KeyError:
                        print(f"Erro ao calcular distância entre os pontos {ponto1} e {ponto2}")
                    print(f"Distância entre Ponto {posicao1} e Ponto {posicao2}: {distancia:.2f}")
        return matriz_dist
