# Gabriel Thiago
# RA: 107774

def BFS(G,s):
    qtd = len(G)                           #quantidade de vertice

    branco = "B"
    preto = "P"
    cinza = "C"

    cor = [branco for x in range(qtd)]     #inicializa as cores com Branco
    D = [-1 for x in range(qtd)]            #zera as distancias
    D[s] = 0

    cor[s] = cinza                         #define o vertice "s" com Cinza

    i = 0                                  #indice para lista Q
    Q  = []                                #lista p verificacao
    Q.append(s)                            #insere o "s" na lista

    while (len(Q) != i):
        u = Q[i]                           #"u" obtem valor para verificar
        i+=1                               #indice para o proximo valor

        for v in G[u]:
            if cor[v] == branco:
                D[v] = D[u] + 1
                cor[v] = cinza
                Q.append(v)

        cor[u] = preto

    return D
