from astar_grid import AStarGrid, AStarGridNode
from itertools import product
 
# Criando o grafo a ser usado no A estrela
# Os nodos que representariam os obstaculos sao eliminados do grafo
def boardGraph(infor):
    
    grafo = {}
    nodo = [[AStarGridNode(x, y) for y in range(infor['altura'])] for x in range(infor['largura'])]

    for x, y in product(range(infor['largura']), range(infor['altura'])):
        
        node = nodo[x][y]
        grafo[node] = []

        for i, j in product([-1, 0, 1], [-1, 0, 1]):
    
            if [ x + i, y + j] in infor['obstaculos']: continue            
            if not (0 <= y + j < infor['altura']): continue
            if not (0 <= x + i < infor['largura']): continue
            if(i == -1 and j == -1 or i == -1 and j == 1 or i == 1 and j == -1 or i == 1 and j == 1 ): continue 

            grafo[nodo[x][y]].append(nodo[x + i][y + j])

    return nodo, grafo
