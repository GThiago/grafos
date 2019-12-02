# Gabriel Thiago
# RA: 107774

def minimo(Q,key,visit):                              #Minimo em Q pela key
    aux = key
    i=0
    while i < len(aux):
        x= aux.index(min(aux))
        onde = x
        if visit[onde] == -1:
            return onde
        i+=1
        aux[onde] = 101                        #Qualquer numero maior q 1

def MST_prim(G,w,r):
    tam = len(G)


    #inicializacao
    A = [[] for _ in range(tam)]             #declara grafo adj G com "n" vertices
    key = [100 for _ in range(tam)]          #qualquer num maior q 1
    parent = [-1 for _ in range(tam)]        #pi
    Q = [x for x in range(tam)]
    visit = [-1 for _ in range(tam)]

    key[r] = 0

    while len(Q) > 0:
        u = minimo(Q,key,visit)
        Q.remove(u)
        visit[u] = 1

        if parent[u] != -1:
            A[parent[u]].append(u)
            A[u].append(parent[u])

        for v,peso in enumerate(G[u]):
            if peso != -1:
                if visit[v] == -1 and peso < key[v]:
                    parent[v] = u
                    key[v] = peso

    return A
