from xmlrpc.client import Binary

from pyomo.environ import *

model = ConcreteModel()

# Instance 1
J = 5
K = [6840, 2637, 2786, 2912, 1683] #Capacidades de J
I = 25
e = [1872, 124, 124, 124, 124, 1872, 124, 1872, 1872, 124, 124, 124, 124, 1872, 124, 124, 124, 124, 124, 124, 124, 124,
     1872, 1872, 124] #Demandas de I
d = [
        [560, 6140, 7090, 7850, 11670],
        [2380, 4720, 5440, 6260, 11010],
        [4520, 3830, 4090, 4900, 10390],
        [6960, 4090, 3650, 4220, 10130],
        [9530, 5770, 4890, 5060, 10620],
        [1650, 5570, 6670, 7310, 10130],
        [2750, 3050, 4110, 4800, 8540],
        [4770, 1140, 1960, 2730, 7650],
        [7050, 2110, 1200, 1630, 7540],
        [9680, 4600, 3480, 3230, 8120],
        [4340, 5650, 6770, 7160, 8250],
        [4920, 3430, 4470, 4760, 6320],
        [6280, 1840, 2520, 2570, 5080],
        [8230, 2560, 1960, 1210, 4740],
        [10330, 4640, 3620, 2890, 5880],
        [6950, 6900, 7860, 8000, 7050],
        [7270, 5140, 5920, 5870, 4740],
        [8380, 4370, 4730, 4390, 2770],
        [9840, 4750, 4550, 3870, 2080],
        [11850, 6250, 5580, 4760, 3700],
        [9170, 8370, 9190, 9150, 6600],
        [9620, 7200, 7780, 7530, 4060],
        [10590, 6930, 7200, 6750, 1950],
        [11750, 7090, 7000, 6330, 630],
        [13400, 8120, 7700, 6900, 3000]
    ]
M = max(e) * max([max(row) for row in d]) * J
S = 999999999

# Laravel X = Instalar ou não o local de votação
model.x = Var(range(J), domain=Binary)
# Laravel Y = Demanda i é atendida por j ou não
model.y = Var(range(I), range(J), domain=Binary)

# Função objective
model.obj = Objective(expr=sum([M * model.x[i] for i in range(J)]) + sum([e[i] * d[i][j] * model.y[i, j]
                                                                          for i in range(I) for j in range(J)]))

model.cons = ConstraintList()

# Restriction 1 Conforme visto em aula tem que estar em formato de lista, pq se não ele só adiciona 1 na con1, tem que ser uma lista de condição para cada restrição;
for i in range(I):
    model.cons.add(sum(model.y[i, j] for j in range(J)) == 1)

# Restriction 2
model.cons.add(sum([e[i] * model.y[i, j] for i in range(I) for j in range(J)]) <= sum(K[j] * model.x[j]
                                                                                                     for j in range(J)
                                                                                                     ))
# Restriction 3
model.cons.add(sum(model.y[i, j] * d[i][j] for i in range(I) for j in range(J)) <= S)

# Solutes
opt = SolverFactory('glpk')
opt.solve(model, timelimit=300).write()
print(model.obj.expr())

# Impair valor's x
print("Valor's x:")
for i in range(J):
    print(f"x[{i}] = {model.x[i].value}")

# Impair valor's y
print("\nValor's y:")
for i in range(I):
    for j in range(J):
        print(f"y[{i},{j}] = {model.y[i,j].value}")
