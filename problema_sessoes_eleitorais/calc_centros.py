import math

class calc_centros:
    def calcular_centros_setores(n, L):
        raizN = int(math.sqrt(n))
        centros = []
        for i in range(0, raizN):
            for j in range(0, raizN):
                x = ((i + 0.5)/raizN) * L
                y = ((j + 0.5)/raizN) * L
                centros.append((x, y))
        return centros

    def calc_pos_central(L):
      x = L/2;
      y = L/2;
      pos_central = []
      pos_central.append((x, y))
      return pos_central

    centros = calcular_centros_setores(25, 1000)
    print(centros)

    pos_central = calc_pos_central(1000)
    print(pos_central)
