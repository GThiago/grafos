# Gabriel Thiago
# RA: 107774

from arvore import eh_arvore
from diametro import diametro
from MST_prim import MST_prim

def testeMstPrim():
    w=[]
    r = 0

    G = [[-1] * 4 for _ in range(4)]             #declara grafo adj G com "n" vertices

    w.append([0,1, 0.655])
    w.append([0,2, 0.251])
    w.append([1,3, 0.654])
    w.append([2,3, 0.541])
    w.append([1,2, 0.751])
    w.append([0,3, 0.161])

    G[0][1] = 0.655
    G[1][0] = 0.655
    G[0][2] = 0.251
    G[2][0] = 0.251
    G[0][3] = 0.161
    G[3][0] = 0.161
    G[1][2] = 0.751
    G[2][1] = 0.751
    G[1][3] = 0.654
    G[3][1] = 0.654
    G[2][3] = 0.541
    G[3][2] = 0.541

    A = MST_prim(G,w,r)
    assert A == [[3, 2], [3], [0], [0, 1]]
    assert eh_arvore(A)
