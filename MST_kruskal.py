# Gabriel Thiago
# RA: 107774

from operator import itemgetter
from funcoes_Kruskal import find_set,union

def mst_kruskal(G,w):
    A = [[] for _ in range(len(G))]              #Lista Adj do caminho minimo com "n" vertice

    ordem = [0 for _ in range(len(G))]           #make_set
    p = [x for x in range(len(G))]               #make_set

    if w == []:
        for x,linha in enumerate(G):
            for y,peso in enumerate(linha):
                if (peso != ""):
                    w.append([x,y,peso])          #coloca os peso em W


    w.sort(key = itemgetter(2))                  #peso ordenado em (u, v, w)

    for (a,b,_) in w:                                  #para cada aresta em ordem
        if find_set(a,p) != find_set(b,p):
            A[a].append(b)
            A[b].append(a)
            union(a, b, ordem,p)
    return A
