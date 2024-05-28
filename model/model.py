from database.DAO import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._grafo = nx.Graph()



    def getNazioni(self):
        return DAO.getNazioni()
    def getAnni(self):
        return DAO.getAnni()

    def buildGraph(self, nazioneSelezionata, anno):
        retailers = DAO.getAllNodes(nazioneSelezionata) #lista di tutti i nodi
        self._grafo.add_nodes_from(retailers)
        listaDafiltrare = self.getAllEdges(int(anno))
        for tupla in listaDafiltrare:
            v0 = tupla[0]
            v1 = tupla[1]
            peso = tupla[2]
            if self._grafo.has_edge(v0, v1):
                self._grafo[v0][v1]['weight'] += peso
            else:
                self._grafo.add_edge(v0, v1, weight=peso)






    def getAllEdges(self, anno):
        return DAO.getAllEdges(anno)


    def getNumEdges(self):
        return len(self._grafo.edges)
    def getNumNodes(self):
        return len(self._grafo.nodes)
