import random
import numpy as np

class xorshift:
    x = 123456789
    y = 362436069
    z = 521288629
    w = 88675123
    
    
    def __init__(self,seed):
        for _ in range(seed):
            self.get()
    
    def get(self):
        t = (self.x^(self.x<<11))
        t &= 0xFFFFFFFF
        self.x,self.y,self.z = self.y,self.z,self.w
        self.w=((self.w ^ (self.w >> 19)) ^ (t ^ (t >> 8)))
        self.w &= 0xFFFFFFFF
        return self.w

np.random.seed(seed=0)
randxor = xorshift(0)

    

#5人*4グループ*30ラウンドのランダムマッチングを行う
players_per_group = 5
num_groups = 4
num_rounds = 30

#ポアソン分布
#np.random.poisson(5)
#幾何分布
#np.random.geometric(0.25) (+1?)

matching_matrix = [[[] for i in range(num_groups)] for j in range(num_rounds)]
for rounds in range(num_rounds):
    left_group_id = [i for j in range(players_per_group) for i in range(num_groups)]
    for player in range(players_per_group*num_groups):
        idx = randxor.get()%len(left_group_id)
        matching_matrix[rounds][left_group_id[idx]].append(player+1)
        left_group_id.pop(idx)
        

"""
def xorshift(generator, seed=None):
    ret = seed
    def inner():
        nonlocal ret
        if ret is None:
            ret = generator()
        else:
            ret = generator(*ret)
        return ret[-1]
    return inner
def xor128(x=123456789, y=362436069, z=521288629, w=88675123):
    t = x ^ (x << 11) & 0xFFFFFFFF
    x = y
    y = z
    z = w
    w = (w ^ (w >> 19)) ^ (t ^ (t >> 8)) & 0xFFFFFFFF
    return x, y, z, w

randxor = xorshift(xor128,random.randrange(100))
"""