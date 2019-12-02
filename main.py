#--------------------------------------------------------------------------------------
#   Disciplina: Algoritmos em grafos - 6898
#   Professor: Marco A. L. Barbosa
#   Aluno: Gabriel Thiago H. Dos Santos
#   RA: 107774
#
#   Execucao
#   Para testes de BFS/Diametro/Arquivo do RandomWalk = pynthon3 codigo randomwalk
#   Para testes de eh_arvore/MST_prim/Arquivo do Prim = pynthon3 codigo kruskal
#   Para testes de MST_kruskal/arquivo do Kruskal = pynthon3 codigo prim
#   Para TODOS os testes = pynthon3 codigo todos
#--------------------------------------------------------------------------------------

import sys
from arquivo import testeArquivo
from testeMstKruskal import testeMstKruskal
from testeMstPrim import testeMstPrim
from testesBFS import testes

def main():
    comando = sys.argv[1].lower()

    if (comando == 'randomwalk') or (comando == 'randonwalk'):
        randonWalk()

    elif comando == 'kruskal':
        kruskal()

    elif comando == 'prim':
        prim()

    elif comando == 'todos':
        randonWalk()
        print()
        kruskal()
        print()
        prim()

    else:
        print("\n\t ~~~~~~~~~~~~~\t\t ~~~~~~~~~~~~~~~~~\t\t~~~~~~~~~~~~~~~~~")
        print("| Para testes de BFS/Diametro/Arquivo do RandomWalk = 'pynthon3 codigo randomwalk|'\n")
        print("| Para testes de eh_arvore/MST_prim/Arquivo do Prim = 'pynthon3 codigo kruskal'\t |\n")
        print("| Para testes de MST_kruskal/arquivo do Kruskal = 'pynthon3 codigo prim'\t |\n")
        print("| Para TODOS os testes = 'pynthon3 codigo todos'\t\t\t\t |")
        print("\t ~~~~~~~~~~~~~\t\t ~~~~~~~~~~~~~~~~~\t\t~~~~~~~~~~~~~~~~~\n")

def randonWalk():
    testes()
    print ("BFS e diametro testado!")
    testeArquivo("randonwalk")

def kruskal():
    testeMstKruskal()
    print ("MST_kruskal e eh_arvore testado!")
    testeArquivo("kruskal")

def prim():
    testeMstPrim()
    print ("MST_prim testado")
    testeArquivo("prim")

if __name__ == "__main__":
    main()
