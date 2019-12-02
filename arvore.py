# Gabriel Thiago
# RA: 107774

from BFS import BFS
from Arestas import arestas

def eh_arvore(G):
    aresta = arestas(G)

    if (aresta != len(G)-1):
        return False

    s = 0
    D = BFS(G,s)

    return -1 not in D
