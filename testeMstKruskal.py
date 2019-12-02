# Gabriel Thiago
# RA: 107774

from MST_kruskal import mst_kruskal
from arvore import eh_arvore

def testeMstKruskal():
    #Representacao do Grafo
    #        8       7
    #     b ---- c ---- d
    #  4/ |     /  \    | \9
    # a   |11  i   4\ 14|   e
    #  8\ |  /  \     \ | /10
    #     h ---- g ---- f
    #        1      2

    a = 0
    b = 1
    c = 2
    d = 3
    e = 4
    f = 5
    g = 6
    h = 7
    i = 8

    G = [[""] * 9 for _ in range(9)]

    G[a][b] = 4
    G[a][h] = 8

    G[b][a] = 4
    G[b][c] = 8
    G[b][h] = 11

    G[c][b] = 8
    G[c][d] = 7
    G[c][i] = 2
    G[c][f] = 4

    G[d][c] = 7
    G[d][e] = 9
    G[d][f] = 14

    G[e][d] = 9
    G[e][f] = 10

    G[f][d] = 14
    G[f][e] = 10
    G[f][c] = 4
    G[f][g] = 2

    G[g][f] = 2
    G[g][i] = 6
    G[g][h] = 1

    G[h][g] = 1
    G[h][i] = 7
    G[h][a] = 8
    G[h][b] = 11

    G[i][h] = 7
    G[i][c] = 2
    G[i][g] = 6

    w = []
    A = mst_kruskal(G,w)

    assert A == [[1, 7], [0], [8, 5, 3], [2, 4], [3], [6, 2], [7, 5], [6, 0], [2]]
    assert eh_arvore(A)

testeMstKruskal()
