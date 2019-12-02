# Gabriel Thiago
# RA: 107774

from BFS import BFS
from diametro import diametro

def teste1():

    #Representacao do Grafo
    # 0 --- 1
    # |
    # 2 --- 3

    G = [
        [1,2],         #0
        [0],           #1
        [0,3],         #2
        [2]            #3
    ]

    assert BFS(G,1) == [1,0,2,3]           #vertice com indice [0,1,2,3]
    assert diametro(G) == 3

def teste2():

    #Representacao do Grafo
    # 0---1---2
    #     |
    # 3---4---5

    G = [
        [1],           #0
        [0,2,4],       #1
        [1],           #2
        [4],           #3
        [1,3,5],       #4
        [4]            #5
    ]

    assert BFS(G,0) == [0,1,2,3,2,3]
    assert diametro(G) == 3

def teste3():

    #Representacao do Grafo
    # 0   1---2
    # |       |
    # 3-------4---5

    G = [
        [3],           #0
        [2],           #1
        [1,4],         #2
        [0,4],         #3
        [2,3,5],       #4
        [4]            #5
    ]

    assert BFS(G,4) == [2,2,1,1,0,1]
    assert diametro(G) == 4

def teste4():

    #Representacao do Grafo
    #        0
    #        |
    #   2----1----4
    #   |    |    |
    #   |    3    |
    #   |         |
    #   5----6    7

    G = [
        [1],           #0
        [0,2,3,4],     #1
        [1,5],         #2
        [1],           #3
        [1,7],         #4
        [2,6],         #5
        [5],           #6
        [4],           #7
    ]

    assert BFS(G,0) == [0,1,2,2,2,3,4,3]
    assert BFS(G,3) == [2,1,2,0,2,3,4,3]
    assert diametro(G) == 5

def teste5():

    #Representacao do Grafo
    #   2-----3
    #   |     |
    #   1     4----6
    #   |     |    |
    #   0     5    7

    G=[
        [1],           #0
        [0,2],         #1
        [1,3],         #2
        [2,4],         #3
        [3,5,6],       #4
        [4],           #5
        [4,7],         #6
        [6]            #7
    ]

    assert BFS(G,0) == [0,1,2,3,4,5,5,6]
    assert diametro(G) == 6

def teste6():

    #Representacao do Grafo
    # 0 --- 1
    # |     |
    # 2 --- 3 --- 4

    G = [
    [1,2],         #0
    [0,3],         #1
    [0,3],         #2
    [1,2,4],       #3
    [3]            #4
    ]

    assert BFS(G,0) == [0,1,1,2,3]         #teste BFS com grafo com ciclo
    assert BFS(G,1) == [1,0,2,1,2]

def teste7():

    #Representacao do Grafo
    # 0 --- 1    2
    # |     |    | \
    # 3     4    5  6

    G = [
    [1,3],         #0
    [0,4],         #1
    [5,6],         #2
    [0],           #3
    [1],           #4
    [2],           #5
    [2]            #6
    ]

    assert BFS(G,0) == [0,1,-1,1,2,-1,-1]         #teste BFS com grafo com desconexo
    assert BFS(G, 5) == [-1,-1,1,-1,-1,0,2]

#chamada dos testes
def testes():
    teste1()
    teste2()
    teste3()
    teste4()
    teste5()
    teste6()
    teste7()
