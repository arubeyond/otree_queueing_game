import random
import numpy as np

np.random.seed(seed=0)


#ポアソン分布
#np.random.poisson(5)
#幾何分布
#np.random.geometric(0.25) (+1?)


def make_matching():
    R = 2
    N = 4
    G = [2 for r in range(R)]
    
    #for r in range(R):
    #    while True:
    #        G[r] = np.random.poisson(5)
    #        if G[r]<=N:break
    
    B = [(n+1) for n in range(N)]
    matrix = [[] for r in range(R)]
    for r in range(R):
        g = G[r]
        matrix[r].append([])
        ids = [(n+1) for n in range(N)]
        for i in range(N%g):
            idx = np.random.randint(len(B))
            ids.remove(B[idx])
            matrix[r][0].append(B.pop(idx))
            if B.empty():B = [(n+1) for n in range(N)]
        np.random.shuffle(ids)
        for i in range(N//g):
            matrix[r].append(ids[i*g:(i+1)*g])
    #休みを平均化したもの、R,N,Gを内生化
    return matrix
        

