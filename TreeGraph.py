from TutorFile.Stack import PilaArrayList
from TutorFile.base import *
from TutorFile.Queue import CodaArrayList as Queue

class NodeForTree(Node):
    #Nodo modificato per permettere la creazione dell'albero
    def __init__(self,id,value):#mod
        super(Node,self).__init__()
        self.id = id
        self.value= value
        self.visit = 0
        self.height = 0
        self.father = None
        self.son = []
        self.leaves=0
        self.superFather=[]
        self.average=0

    def reset(self):#mod
        #questa funzione imposta ai valori iniziali tutti i moduli del nodo per la creazione di un nuovo albero
        self.visit = 0
        self.height = 0
        self.father = None
        self.son = []
        self.leaves=0
        self.superFather=[]

class Tree():

    def __init__(self, rootNode=None):
        self.root = rootNode

    def addNode(self,father,son):#mod
        #aggiunge un nodo all'albero
        if not father.son.__contains__(son):
            father.son.append(son)
            son.father=father
            son.height=father.height+1

    def stampa(self):
        #Permette di stampare l'albero. Per farlo si usa una pila di appoggio
        stack = PilaArrayList()
        stack.push([self.root, 0])  # pila di liste di due elementi [il nodo, il livello occupato dal nodo]
        while not stack.isEmpty():
            current = stack.pop()
            level = current[1]
            print("|---" * level + str(current[0]))
            for son in current[0].son:
                stack.push([son, level + 1])
