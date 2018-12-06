from AverageNode import *
def prova():
    a=GraphNO()
    for i in range(11):
        a.addNode('value')
    a.insertEdgeNO(0,6)
    a.insertEdgeNO(0,4)
    a.insertEdgeNO(6,3)
    a.insertEdgeNO(4,8)
    a.insertEdgeNO(4,2)
    a.insertEdgeNO(4,1)
    a.insertEdgeNO(1,9)
    a.insertEdgeNO(1,7)
    a.insertEdgeNO(1,3)
    a.insertEdgeNO(8,5)
    a.insertEdgeNO(2,5)
    a.insertEdgeNO(5,10)
    return a

def average(graph,nodeMid):
    tree=graph.BFSMod(nodeMid)
    for curr in graph.getNodes():
        curr=graph.getNode(curr)
        father=curr
        list=Queue()
        heightFather=curr.height
        while curr.height < 2*heightFather :
            if not curr.son==[]:
                for son in curr.son:
                    if not list.q.__contains__(son):
                        list.enqueue(son)
            if list.q==[] or list.q[0].height==2*heightFather :
                break
            curr=list.dequeue()
        father.average+=len(list.q)

def averageNode(graph):
    for node in graph.getNodes():
        graph.getNode(node).average=0
    list=[]
    for node in graph.getNodes():
        average(graph,node)
    for node in graph.getNodes():
        list.append([node,graph.getNode(node).average])
        if len(list)>1:
            if list[0][1]< list[1][1]:
                list.pop(0)
            else:
                list.pop(1)
    return [list[0][0],int((list[0][1])/2)]

if __name__ == "__main__":
    print('Nodo medio di un grafo casuale con 10 nodi e 20 archi')
    graph = makeCasualGraph(10, 20)
    print(averageNode(graph))
    graph=makeCasualGraph(100,200)
    print('Nodo medio di un grafo casuale con 100 nodi e 200 archi')
    print(averageNode(graph))
    graph = makeCasualGraph(300, 600)
    print('Nodo medio di un grafo casuale con 300 nodi e 600 archi')
    print(averageNode(graph))


