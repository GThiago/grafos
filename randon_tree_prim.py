# Gabriel Thiago
# RA: 107774

from operator import itemgetter
from MST_prim import MST_prim
from random import random

def randon_tree_prim(n):
    w = []
    r = 0
    G = [[""] * n for _ in range(n)]             #declara grafo adj G com "n" vertices

    for x in range(n-1):                         #gera os pesos em G
        for y in range(n-1,x,-1):
            num = random()
            G[x][y] = num
            G[y][x] = num
            w.append([x,y,num])                 #coloca os peso em W

    A = MST_prim(G,w,r)

    return A
