from GraphNO import *
from math import fsum,sqrt
from random import *
from time import *
def makePerfectGraph(n):                                     #questa funzione crea un grafo con n nodi perfetto
    graph=GraphNO()                                     #crea un grafo vuoto
    for i in range(n):
        graph.addNode('value')                          #aggiunge n nodi
    for i in range(n):
        for e in range(i,n):
           graph.insertEdgeNO(i,e)                      #collega ogni nodo con tutti gli altri
    return graph

def makeCasualGraph(n,m):                                     #questa funzione crea un grafo con n nodi e m archi casuale
    graph=GraphNO()                                     #crea un grafo vuoto
    for i in range(n):
        graph.addNode('value')                          #aggiunge n nodi
    for i in range(m):
        graph.insertEdgeNO(randint(0,n),randint(0,n))   #aggiunge m archi al grafo tra nodi casuali

    return graph

def addLeaves(node):
    #questa funzione calcola il numero di foglie che i sottoalberi con radice di altezza 1 hanno in un determinato livello
    #un superFather e' un nodo x di altezza 1
    leaves=len(node.son)     #numero di figli del nodo corrente
    if node.height==1:
        node.superFather=node #se stiamo visitando i nodi di altezza 1 loro stessi sono i superFather
    elif node.height ==2:
        node.superFather=node.father #se stiamo visitando i nodi di altezza 2 i superFather sono i loro padri
    elif node.height>2:
        node.superFather=node.father.superFather    #se stiamo visitando i nodi di altezza >2 i superFather sono gli stessi superFather dei loro padri
    if node.height != 0:
        node.superFather.leaves+=leaves             #se non stiamo visitando la radice aggiungiamo i figli del nodo corrente al superFather

def combination(list,graph):
    #questa funzione data una lista di nodi e un grafo crea una lista dove mette il numero di foglie dei nodi dati, poi *(scritto sotto)
    list2=[]
    for i in range(len(list)):
        list2.append(graph.getNode(list[i]).leaves)   #agginge alla lista il numero di foglie di ogni nodo
    totalCouple = 0
    for i in range(len(list2)):
        totalCouple += ((list2[i]) * fsum(list2[i + 1:])) # * moltiplica il numero di foglie del nodo per la somma di quelli rimanenti non considerando nella somma quelli gia' calcolati
    return int(totalCouple)

def average(graph, nodeM):
    #questa funzione dato un grafo e un nodo, calcola per quante coppie di nodi il nodo e' medio
    average=0
    degRoot=graph.deg(nodeM.id)
    if degRoot <= 1:
        return nodeM,0                                                          #se il grado del nodo nodeM e' 0 o 1, questo non puo' essere medio per nessuna coppia di nodi
    tree=Tree(nodeM)                                                            #creo un albero con radice nodeM
    graph.reset()                                                               #resetteiamo tutti i nodi del grafo ai valori iniziali
    nodeM.visit = 1                                                             #settiamo il marcatore visit a 1 per indicare all'algoritmo di non ripeterlo
    average = int((degRoot*(degRoot-1))/2)                                #calcolo le combinazioni di coppie con distanza 1 per cui nodeM e' medio usando la serie aritmetica sul grado di nodeM -1
    list = Queue()                                                              #creo una coda
    nSon = graph.getAdj(nodeM.id)                                               #creo una lista di 'superFather' cioe' di nodi con altezza 1
    curr = nodeM.id                                                               #inizializzo curr (nodo corrente) alla radice
    changeLevel=2                                                                 #inizializzo contatore di cambio livello a 2(livello=altezza albero)

    while curr != None:                                                           #il ciclo continua fino all'ultima foglia dell'albero(considera tutti i nodi del grafo)
        for node in graph.dicE[curr]:                                             #il ciclo prende tutti i nodi adiacenti a curr
            if graph.getNode(node).visit == 0:                                  #se il nodo non e' mai stato visitato...
                tree.addNode(graph.getNode(curr), graph.getNode(node))            #lo aggiunge all'albero (marca il nodo figlio node come visitato,imposta l'altezza a curr.height+1,aggiunge node alla lista figli di curr,imposta curr come padre di node )
                list.enqueue(node)                                              #aggiungo node alla coda

        if changeLevel == graph.getNode(curr).height:                         # controlla se l'altezza del nodo corrente e' uguale al contatore
            list2=[]
            for i in range(len(nSon)):
                list2.append(graph.getNode(nSon[i]).leaves)
            sum=fsum(nSon)
            average += int((sum*(sum-1))/2)                           #aggiunge le coppie del livello changeLevel al contatore average
            for node in nSon:
                graph.getNode(node).leaves = 0                                  # azzero le foglie dei superFather
            changeLevel += 1                                                     #imposta il prossimo cambio livello al livello +1

        addLeaves(graph.getNode(curr))                                            # aggiungo i filgi di node al superFather
        print(curr)
        curr = list.dequeue()                                                     #imposto il nodo corrente come il primo nodo della coda e lo elimino
    return [nodeM,average]

def averageNode(graph):
    #
    list=[]
    for node in graph.getNodes():
        list.append(average(graph,graph.getNode(node)))  #appende alla lista la sottolista composta dal nodo e il valore di quante volte e' medio
        if len(list)>1:
            if list[0][1] < list[1][1]:
                list.pop(0)                             #se e' maggiore il valore del nodo appena inserito, elimina il primo
            else:
                list.pop(1)                             #altrimenti elimina quello appena inserito
    return [list[0][0].id,list[0][1]]

def tempo(n):
    graph=makeCasualGraph(n)
    start=clock()
    averageNode(graph)
    end=clock()-start
    return end

def mediaEdge(graph):
    tot=0
    for node in graph.getNodes():
        tot+=len(graph.dicE[node])
    return tot


if __name__ == "__main__":
    p = None
    while p != 0:
        p = int(input("\n  Per entrare nel programma digita 1 per uscire digita 0: "))
        if p == 1:
            print('\n  Questo programma genera un grafo non orientato')
            numNodes = int(input('\n  Quanti nodi vuoi? '))
            numEdges = int(input('\n  Quanti archi vuoi? '))
            graph=makeCasualGraph(numNodes,numEdges)
            p = int(input("\n  Per vedere il grafo digita 1 altrimenti 0:  "))
            if p == 0:
                pass
            elif p == 1:
                print("\n  1. Questo e' il grafo\n")
                graph.print1()
            else:
                print("\n  Mi dispiace scelta non supportata")
                break

            p = int(input("\n  Digita 1 se vuoi vedere l'albero del nodo medio 0 se desideri sapere solo il numero di coppie: "))
            node=averageNode(graph)
            if p == 1:
                print('\n il nodo',node[0],'ha ',node[1],'coppie')
                graph.BFS(node.id).stampa()
            elif p == 0:
                print('\n il nodo', node[0], 'ha ', node[1], 'coppie')
            else:
                print("\n  Mi dispiace scelta non supportata")
                break
        elif p == 0:
            break
        else:
            print("\n  Mi dispiace scelta non supportata")
            break





