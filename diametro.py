# Gabriel Thiago
# RA: 107774

from BFS import BFS

def diametro(T):
    s = 0
    D = BFS(T,s)                           #distancias comparadas ao vertice[0]
    a = D.index(max(D))                    #vertice extremo para nova busca
    distancia = max(BFS(T,a))

    return distancia
