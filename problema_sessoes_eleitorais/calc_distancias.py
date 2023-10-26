import math
class calc_distancias:
  def calc_distancias(n, centros):
    raizN = int(math.sqrt(n))
    for i in range(n):
        for j in range(n):
            ponto1, ponto2 = centros[i], centros[j]
            if ponto1 == ponto2:
                distancia = 0
            else:
                try:
                    posicao1 = ((i // raizN + 1 - 1), (i % raizN + 1 - 1))
                    posicao2 = ((j // raizN + 1 - 1), (j % raizN + 1) - 1)
                    x1, y1 = ponto1
                    x2, y2 = ponto2
                    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                except KeyError:
                    print(f"Erro ao calcular distância entre os pontos {ponto1} e {ponto2}")
                print(f"Distância entre Ponto {posicao1} e Ponto {posicao2}: {distancia:.2f}")


