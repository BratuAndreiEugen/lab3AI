# evaluate the quality of previous communities inside a network
# https://www.cs.cmu.edu/~ckingsf/bioinfo-lectures/modularity.pdf

def modularity(communities, param): # Q
    noNodes = param['noNodes']
    mat = param['matrix']
    degrees = param['degrees']
    noEdges = param['noEdges']
    M = 2 * noEdges
    Q = 0.0
    for i in range(0, noNodes):
        for j in range(0, noNodes):
            if (communities[i] == communities[j]):
               Q += (mat[i][j] - degrees[i] * degrees[j] / M)
    return Q * 1 / M

def modularity1(communities, param): # D
    noNodes = param['noNodes']
    mat = param['matrix']
    degrees = param['degrees']
    noEdges = param['noEdges']
    d = {}
    L = {}
    notL = {}
    for i in range(0, len(communities)):
        if d.get(communities[i]) != None:
            d[communities[i]] += 1
        else:
            d[communities[i]] = 1
            L[communities[i]] = 0
            notL[communities[i]] = 0


    D = 0.0

    for i in range(0, noNodes):
        for j in range(0, noNodes):
            if communities[i] == communities[j]:
                L[communities[i]] += 1
            else:
                notL[communities[i]] += 1
                notL[communities[j]] += 1
    for i in set(communities):
        D += (L[i]/d[i] - (notL[i]/2)/d[i])
    return D



def modularity2(communities, param): # CS
    noNodes = param['noNodes']
    mat = param['matrix']
    degrees = param['degrees']
    noEdges = param['noEdges']
    CS = 0.0
    alpha = 10
    d = {}
    score = {}
    L = {}
    for i in range(0, len(communities)):
        if d.get(communities[i]) != None:
            d[communities[i]] += 1
        else:
            d[communities[i]] = 1
            score[communities[i]] = 0
            L[communities[i]] = 0

    for i in range(0, noNodes):
        suma = 0
        for j in range(0, noNodes):
            if communities[i] == communities[j]:
                suma += mat[i][j]
                L[communities[i]] += 1
        score[communities[i]] += (suma/d[communities[i]])**alpha

    for i in set(communities):
        CS += (score[i]*(L[i]/d[i]))
    return CS