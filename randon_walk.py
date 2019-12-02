# Gabriel Thiago
# RA: 107774

from random import randint

def randonWalk(n):
                                            #inicializa
    G = [[] for _ in range(n)]              #Grafo com "n" vertice
    visitado = [False for _ in range(n)]    #False como nao visitados

    u = randint(0,n-1)                      #Vertice aleatorio de G
    visitado[u] = True                      #Define como visitado

    i = 0                                   #Quantidade de aresta criada
    while (i < n-1):                        #Criara as arestas
        v = randint(0,n-1)
        if not visitado[v]:
            G[u].append(v)
            G[v].append(u)
            visitado[v] = True
            i+=1
        u = v
    return G
