# MyTronBone

from aEstrelaAbstrato import AEstrela, NodoGrafoAbstrato
from itertools import product
# from math import sqrt

# Noh concreto do grafo
class NodoGrafoConcreto(NodoGrafoAbstrato):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        super(NodoGrafoConcreto, self).__init__()
 
    # atualizacao da funcao custo
    def custo(self, other):
        return 10
 
class AEstrelaConcreto(AEstrela):

    # Implementacao concreta
    # Heuristica utilizada pelo a*
    def heur(self, nodo, goal):
        # Foi empregado a distancia manhattan
        return abs(goal.x - nodo.x) + abs(goal.y - nodo.y)
        # distancia euclidiana
        #return sqrt((goal.x - nodo.x)**2 + (goal.y - nodo.y)**2)


 
# Criando o grafo a ser usado no A estrela
# Os nodos que representariam os obstaculos sao eliminados do grafo
def boardGraph(infor):
    
    grafo = {}
    nodo = [[NodoGrafoConcreto(x, y) for y in range(infor['altura'])] for x in range(infor['largura'])]

    for x, y in product(range(infor['largura']), range(infor['altura'])):
        
        node = nodo[x][y]
        grafo[node] = []

        for i, j in product([-1, 0, 1], [-1, 0, 1]):
            
            # Retirando obstaculos do grafo
            if [ x + i, y + j] in infor['obstaculos']: continue            
            if not (0 <= y + j < infor['altura']): continue
            if not (0 <= x + i < infor['largura']): continue
            # Retirando movimentos na diagonal
            if(i == -1 and j == -1 or i == -1 and j == 1 or i == 1 and j == -1 or i == 1 and j == 1 ): continue 

            grafo[nodo[x][y]].append(nodo[x + i][y + j])

    return nodo, grafo