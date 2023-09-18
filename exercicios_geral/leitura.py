import sys

def salva(nome, notas):
    file = open('.notas.txt', 'a')
    file.write(nome)
    file.write('\n')


n_alunos = int(sys.argv[1])
n_notas = int(sys.argv[2])

lista_notas = []

for aluno in range(n_alunos):
     nome = input('Nome do aluno: ')
     lista_notas = []
     for nota in range(n_notas):
        valor_nota = float(input(f'Informe a nota {nota + 1} do aluno'))
        lista_notas.append(valor_nota)
        salva(nome, lista_notas)


