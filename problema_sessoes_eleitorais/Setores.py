import math


class Setores:
    def calcular_centros_setores(n, L):
        raizN = int(math.sqrt(n))
        setores = {}
        pos = 0
        for i in range(0, raizN):
            for j in range(0, raizN):
                x = ((i + 0.5) / raizN) * L
                y = ((j + 0.5) / raizN) * L
                pos = pos + 1
                chave = 'chave' + str(pos)
                setores[chave] = {'valor': (x, y)}
        return setores

    def calc_pos_central(L):
        x = L / 2;
        y = L / 2;
        pos_central = [(x, y)]
        return pos_central

    def class_setor(pos_central, setores):
        class_setores = {}
        pos_central_x, pos_central_y = pos_central[0]
        for i in range(len(setores)):
            setor = setores['chave' + str(i + 1)]['valor']
            x, y = setor
            chave = 'chave' + str(i)
            if (x < (pos_central_x + 100) and (y <= (pos_central_y + 100))):
                class_setores[chave] = {'valor': 'urb'}
            else:
                class_setores[chave] = {'valor': 'rural'}
        return class_setores
