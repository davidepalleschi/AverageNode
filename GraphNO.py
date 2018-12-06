from TutorFile.Graph import *
from TreeGraph import *
from TutorFile.Queue import CodaArrayList as Queue

class GraphNO(Graph):
    #Grafo Non Orientato
    def __init__(self):
        super(GraphNO,self).__init__()

    def insertEdgeNO(self,tail,head):
        #inserisce un arco Non Orientato
        self.insertEdge(tail,head)
        self.insertEdge(head,tail)

    #Override
    def addNode(self, elem):
        #modulo addNode modificato per aggiungere un NodeForTree invece del Node
        node = NodeForTree(self.numId, elem)
        self.dicN[self.numId] = node
        self.dicE[self.numId] = {}
        self.numId += 1
        return node

    def reset(self):
        #questa funzione resetta tutti i nodi del grafo
        for node in self.getNodes():
            self.getNode(node).reset()

    def BFS(self, rootId,nodeB=None):
        self.reset()
        tree=Tree(self.getNode(rootId))
        n1=rootId
        self.getNode(rootId).visit=1
        list=Queue()
        while n1 != nodeB:
            for node in self.dicE[n1]:
                if self.getNode(node).visit == 0:
                    tree.addNode(self.getNode(n1),self.getNode(node))
                    self.getNode(node).visit = 1
                    list.enqueue(node)
            n1=list.dequeue()
        return tree


    def BFSMod(self, rootId,nodeB=None):
        #nella versione modificata del BFS due nodi allo stesso livello possono avere lo stesso figlio
        self.reset()
        tree=Tree(self.getNode(rootId))
        n1=rootId
        self.getNode(rootId).visit=1
        list=Queue()
        res=0
        while n1 != nodeB:
            for node in self.dicE[n1]:
                if self.getNode(node).visit == 0 or self.getNode(node).visit == 2:
                    self.getNode(node).visit = 2
                    tree.addNode(self.getNode(n1),self.getNode(node))
                    list.enqueue(node)
            if self.getNode(n1).height==res:
                self.getNode(n1).visit = 1
                for node in list.q:
                    self.getNode(node).visit=1
                res+=1

            n1 = list.dequeue()
            if n1 != None:
                if self.getNode(n1).height==res:
                      self.getNode(n1).visit = 1
                      for node in list.q:
                         self.getNode(node).visit=1
                      res+=1
        return tree


    def dist(self,nodeAId,nodeBId):
        tree=self.BFS(nodeAId,nodeBId)
        return self.getNode(nodeBId).height

if __name__ == "__main__":
    print('Grafo non orientato')
    graph=GraphNO()
    graph.addNode('value')
    graph.addNode('value')
    graph.insertEdgeNO(0,1)
    graph.BFS(0).stampa()






