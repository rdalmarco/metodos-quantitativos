from pyomo.environ import *

# Criação do modelo
model = ConcreteModel()

# Variáveis de decisão
model.a = Var(domain = NonNegativeReals)
model.b = Var(domain = NonNegativeReals)

# Função objetivo
def objective_function(model):
    return 0.05 * model.a + 0.08 * model.b

model.obj = Objective(rule = objective_function, sense = maximize)

# Restrições
def amount(model):
    return model.a + model.b <= 5000

def max_a(model):
    return 0.75 * model.a - 0.25 * model.b >= 0

def max_b(model):
    return -0.5 * model.a + 0.5 * model.b <= 0

def proportion(model):
    return model.a - 0.5 * model.b >= 0

model.con1 = Constraint(rule = amount)
model.con2 = Constraint(rule = max_a)
model.con3 = Constraint(rule = max_b)
model.con4 = Constraint(rule = proportion)

# Solução
opt = SolverFactory('glpk', executable='/usr/bin/glpsol')
opt.solve(model).write()
print('\n\nSOLUÇÃO ÓTIMA')
print('Investimento A:', model.a())
print('Investimento B:', model.b())
print('Rendimento:', model.obj())