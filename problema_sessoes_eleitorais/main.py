from xmlrpc.client import Binary
from Instancia import *
from pyomo.environ import *

model = ConcreteModel()

Instancia.gera_instancia()

# Instance
J = Instancia.J
K = Instancia.K
I = Instancia.I
e = Instancia.e
d = Instancia.d
M = Instancia.M
S = Instancia.S

print('Capacidade: ' + str(sum(K)))
print('Demanda: ' + str(sum(e)))
print('M: ' + str(M))

# Laravel X = Instalar ou não o local de votação
model.x = Var(range(J), domain=Binary)
# Laravel Y = Demanda i é atendida por j ou não
model.y = Var(range(I), range(J), domain=Binary)

# Função objective
model.obj = Objective(expr=sum([M * model.x[j] for j in range(J)]) + sum([e[i] * d[i][j] * model.y[i, j]
                                                                          for i in range(I) for j in range(J)]))

model.cons = ConstraintList()

# Restriction 1
for i in range(I):
    model.cons.add(sum(model.y[i, j] for j in range(J)) == 1)

# Restriction 2
for j in range(J):
    model.cons.add(sum(e[i] * model.y[i, j] for i in range(I)) <= K[j] * model.x[j])

# Restriction 3
for i in range(I):
    for j in range(J):
       model.cons.add(model.y[i, j] * d[i][j] <= S)

# Solutes
opt = SolverFactory('glpk')
opt.solve(model, timelimit=3000).write()
print(model.obj.expr())

# Impair valor's x
print("Valores x:")
for i in range(J):
    print(f"x[{i + 1}] = {model.x[i].value}")

# Impair valor's y
print("\nValores y:")
for i in range(I):
    for j in range(J):
        if model.y[i,j].value == 1:
         print(f"y[{i + 1},{j + 1}] = {model.y[i,j].value}")
