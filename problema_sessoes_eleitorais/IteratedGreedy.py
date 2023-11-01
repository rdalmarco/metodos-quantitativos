class IteratedGreedy:
    I = 20  # Setores
    J = 3   # Locais
    K = [200, 100, 300]  # Capacidade locais
    numLocInstalar = 2


    @classmethod
    def algoritmo(cls):
        #Solução Vazia:
        cls.X = [0] * cls.J
        Y = [[0 for _ in range(cls.I)] for _ in range(cls.J)]

        #Ideia professor:
        #VetorX : Saida vetor setores atendidos [3, 3, 3, 5, 5]
        #VetorY: Saida vetor escolas instaladas [0, 0, 1, 0, 1]

        #Estrutura de grafos
        #Instala uma escola, joga as demandas dos setores nela conforme sua capacidade, quando
        #encher a capacidade dela, instala outra escola e faz a mesma coisa até acabar as demandas.

        #Elementos Candidatos (Irá preencher Cx com valores de 1 a J, locais candidatos a instalação):
        cx = []
        for i in range(1, cls.J + 1):
            cx.append(i)

        #Elementos candidatos (Irá preencher Cy com valores de 1 a I * J, locais candidatos a atender setores).
        cy = [[0 for _ in range(cls.J)] for _ in range(cls.I)]
        for i in range(0, cls.I):
            value = 1
            for j in range (0, cls.J):
                cy[i][j] = value
                value += 1

        #Função Heurística: G = Semi Gulosa
        #Será selecionado para instalação os 3 locais com maior capacidade, depois 1 deles.
        #Será selecionado para atender um setor i o local com maior capacidade mais perto dele.

        #Construção
        ##Percorre enquanto cx e cy ainda tem possibilidades para teste
        Sx = {}
        for i in range(0, cls.numLocInstalar):
          Sx[i] = {'valor' : 0}
        while (len(cx) != 0 and len(cy) != 0):
           ##Percorre cx (Candidatos a Sx) para definir os melhores lugares
            #Percorre todos os locais em Sx comparando se a capacidade de atendimento é maior
             for j in range(0, len(Sx)):
             #Se a capacidade do local for maior do que a de um instalado substitui
              if cls.K[cx[0] - 1] > Sx[j]['valor']:
               min(Sx.items(), key=lambda d : d['valor'])
               pos = j
               value = cls.K[cx[0] - 1]
             Sx[pos] = value
             cx.pop(0)
        print(Sx)
IteratedGreedy.algoritmo()
