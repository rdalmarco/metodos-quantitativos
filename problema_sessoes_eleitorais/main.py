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
    [10, 14, 12, 13, 11],
    [20, 28, 26, 24, 23],
    [3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5],
    [6, 6, 6, 6, 6],
    [7, 7, 7, 7, 7],
    [8, 8, 8, 8, 8],
    [9, 9, 9, 9, 9],
    [10, 10, 10, 10, 10],
    [11, 11, 11, 11, 11],
    [12, 12, 12, 12, 12],
    [13, 13, 13, 13, 13],
    [14, 14, 14, 14, 14],
    [15, 15, 15, 15, 15],
    [16, 16, 16, 16, 16],
    [17, 17, 17, 17, 17],
    [18, 18, 18, 18, 18],
    [19, 19, 19, 19, 19],
    [20, 20, 20, 20, 20],
    [21, 21, 21, 21, 21],
    [22, 22, 22, 22, 22],
    [23, 23, 23, 23, 23],
    [24, 24, 24, 24, 24],
    [25, 25, 25, 25, 25]
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

# Restriction 1
model.con1 = Constraint(expr=sum([model.y[i, j] for i in range(I) for j in range(J)]) == 1)

# Restriction 2
model.con2 = Constraint(expr=sum([e[i] * model.y[i, j] for i in range(I) for j in range(J)]) <= sum(K[j] * model.x[j]
                                                                                                     for j in range(J)
                                                                                                     ))
# Restriction 3
model.con3 = Constraint(expr=sum(model.y[i, j] * d[i][j] for i in range(I) for j in range(J)) <= S)

# Solutes
opt = SolverFactory('glpk')
opt.solve(model, timelimit=30).write()
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
