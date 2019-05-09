
from gurobipy import *
from numpy import *
import pandas as pd
import re as re

raw = []
data = []


print("digite um valor de instancia de 1 a 5")
instanceValue = int(input())
#
stopVariable = instanceValue
filePath = "FileTests/instancia"+str(instanceValue)+".txt"
print(filePath)
with open(filePath,"r") as f:
    for line in f:
        raw.append(line.replace(' ','\n').split())
    i = 0
    temp = []
    if stopVariable == 4:
        stopVariable = 3.875
    if stopVariable == 5:
        stopVariable = 4.875
    for l in range(1,len(raw)):
        for a in range(len(raw[l])):
            temp.append(int(raw[l][a]))
        i = i + 1
        if i ==int((stopVariable)*8):
            data.append(temp)
            temp = []
            i = 0
           
numT = instanceValue*100
numC = instanceValue*100
#MA = tuplelist([(1.5, 2.5, 3.5),(2.9,3.0,3.7),(2.0,1.8,4.0)]) 

Assignment = random.random((numT,numC))

print(Assignment)
m=Model("Assignment")

X = []
for t in range(numT):
	X.append([])
	for c in range(numC):
		X[t].append(m.addVar(vtype=GRB.BINARY,name="X%d%d"% (t, c)))
m.update()
m.modelSense = GRB.MINIMIZE
constraintT = []
constraintC = []
for t in range(numT):
	constraintT.append(m.addConstr(quicksum(X[t][c] for c in range(numC)) == 1 ,'constraintT%d' % t))
	
for c in range(numC):
	constraintT.append(m.addConstr(quicksum(X[t][c] for t in range(numT)) == 1 ,'constraintC%d' % t))

m.setObjective(quicksum(quicksum([X[t][c]*data[t][c]for c in range(numC)]) for t in range(numT)))
	
m.update()

#m.optimize(mycallback)
m.optimize()


#print 'runtime is',m.Runtime
#for v in m.getVars():
    #print('{} = {}'.format(v.varName, v.x))

#print X