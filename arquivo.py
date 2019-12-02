# Gabriel Thiago
# RA: 107774

import time
from arvore import eh_arvore
from diametro import diametro
from randon_tree_prim import randon_tree_prim
from randon_kruskal import random_tree_kruskal
from randon_walk import randonWalk

def testeArquivo(alg):
    nome = alg + ".txt"

    print(f"Criando arquivo '{nome}'")

    file = open(nome,"w")       #Arq p armazenar result

    #teste para 250, 500, 750, 1000, 1250, 1500, 1750, 2000
    for n in range(250,300,250):
        diametroTotal = 0

        for _ in range(500):                # 500 arvores com "n" V
            if alg == "prim":
                G = randon_tree_prim(n)
            elif alg == "kruskal":
                G = random_tree_kruskal(n)
            elif alg == "randonwalk":
                G = randonWalk(n)
            else:
                print("Erro de leitura do desejado!")
                exit()

            assert eh_arvore(G)
            diametroTotal += diametro(G)

        res = diametroTotal/500               #DiametroMedio
        file.write(f"{n} {res:.3f}\n")      #Escreve no arq o result

    file.close()
