# Gabriel Thiago
# RA: 107774

from random import random
from MST_kruskal import mst_kruskal

def random_tree_kruskal(n):
    G = [[""] * n for _ in range(n)]             #declara grafo adj G com "n" vertices
    w=[]

    for x in range(n-1):                         #gera os pesos em G
        for y in range(n-1,x,-1):
            num = random()
            G[x][y] = num
            G[y][x] = num
            w.append([x,y,num])                 #coloca os peso em W

    A = mst_kruskal(G,w)
    return A
