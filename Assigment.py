# step 0. Import Gurobi
from __future__ import print_function
from gurobipy import *

#Pegando conteudo do arquivo
matrix = tuplelist([(1.5, 2.5, 3.5),(2.9,3.0,3.7),(2.0,1.8,4.0)]) 
# STEP 1. Create an empty model
m = Model()

# STEP 2. Add variables
#x = m.addVar(vtype=GRB.BINARY, name='x')
#y = m.addVar(vtype=GRB.BINARY, name='y')
#z = m.addVar(vtype=GRB.BINARY, name='z')

X = m.addVar(len(matrix), len(matrix),vtype=GRB.BINARY, name='x')
Y = m.addVar(len(matrix), vtype=GRB.BINARY, name='y')

# STEP 3. Commit these changes to the model
m.update()

# STEP 4. Set objective function
#m.setObjective(X+Y, GRB.MINIMIZE)

m.setObjective(sum(Y[i] for i in range(len(matrix))), GRB.MINIMIZE)

# STEP 5. Add constraints
#m.addConstr(x + 2*y + 3*z <= 4)
#m.addConstr(x + y >= 1)

#STEP 6. Solve model.
#m.optimize()

#STEP 7. Examine results
#for v in m.getVars():
#   print('{} = {}'.format(v.varName, v.x))
