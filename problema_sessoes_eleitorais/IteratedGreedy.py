class IteratedGreedy:
    I = 20  # Setores
    J = 3   # Locais
    K = [100, 200, 300]  # Capacidade locais

    @classmethod
    def algoritmo(cls):
        #Solução Vazia:
        cls.X = [0] * cls.J
        Y = [[0 for _ in range(cls.I)] for _ in range(cls.J)]

        #Elementos Candidatos (Irá preencher Cx com valores de 1 a J, locais candidatos a instalação):
        cx = []
        for i in range(1, cls.J + 1):
            cx.append(i)

        #Elementos condicionais (Irá preencher Cy com valores de 1 a I * J, locais candidatos a atender setores).
        cy = [[0 for _ in range(cls.J)] for _ in range(cls.I)]
        value = 0
        for i in range(1, cls.I + 1):
            for j in range (1, cls.J + 1):
                cy[i][j] = value
                value += 1

        #Função Heurística: G = Semi Gulosa
        #Será selecionado para instalação os locais com maior capacidade
        #Será selecionado para atender um setor i o local com maior capacidade mais perto dele.

        #Construção
        ##Percorre enquanto cx e cy ainda tem possibilidades para teste
        Sx = [0] * cls.I
        while (len(cx) != 0 and len(cy) != 0):
           ##Percorre cx (Candidatos a Sx) para definir os melhores lugares
           for i in range((len(cx))):
            #Percorre todos os locais em Sx comparando se a capacidade de atendimento é maior
             for j in range(len(Sx)):
             #Se a capacidade do local for maior do que a de um instalado substitui
              if cls.K[cx[i] - 1] > Sx[j]:
               Sx[j] = cls.K[cx[i] - 1]

IteratedGreedy.algoritmo()
