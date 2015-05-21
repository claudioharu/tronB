# Noh abstrato do grafo
class NodoGrafoAbstrato(object):
    
    def __init__(self):
        
        self.pai = None
        # valor da heuristica
        self.h = 0
        # custo de chegar no noh
        self.g = 0
        

    # custo do movimento
    def custo(self, other):
        raise NotImplementedError

class AEstrela(object):

    def __init__(self, graph):
        self.graph = graph
    
    # Heuristica abstrata 
    def heur(self, nodo, start, goal):
        raise NotImplementedError
        
    def caminho(self, start, goal):
        
        atual = start

        # conjunto de nohs que precisam ser investigados
        conjuntoAberto = set()
        conjuntoAberto.add(atual)

        # conjunto de nohs que nao precisam mais serem investigados
        conjuntoFechado = set()
        
        while conjuntoAberto:
            
            atual = min(conjuntoAberto, key = lambda o: o.g + o.h)

            # o goal foi fechado, logo terminou
            if atual == goal:
                
                path = []

                while atual.pai:
                    path.append(atual)
                    atual = atual.pai
                
                path.append(atual)
                return path[::-1]

            conjuntoFechado.add(atual)
            conjuntoAberto.remove(atual)

            for nodo in self.graph[atual]:

                # nada a ser feito
                if nodo in conjuntoFechado:
                    continue
                
                if nodo in conjuntoAberto:

                    # att do valor do custo do noh
                    gAtualizado = atual.g + atual.custo(nodo)
                    if nodo.g > gAtualizado:
                        nodo.pai = atual
                        nodo.g = gAtualizado
                else:

                    nodo.pai = atual
                    # att do valor do custo do noh
                    nodo.g = atual.g + atual.custo(nodo)
                    # att do valor da heuristica
                    nodo.h = self.heur(nodo, start, goal)

                    conjuntoAberto.add(nodo)

        return None
 
