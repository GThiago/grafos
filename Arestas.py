# Gabriel Thiago
# RA: 107774


def arestas(G):                             #Qtde de aresta num G
    aresta = 0
    aux = []                                #lista aux para arestas

    for linha in G:
        aresta += len(linha)

    return aresta/2
