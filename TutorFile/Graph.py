from TutorFile.base import *


class Graph:
    """
    Graph interface.
    It shows how to simulate interfaces behaviour in Python.
    """
    def __init__(self):
        self.numId=0
        self.dicN={}
        self.dicE={}

    def isEmpty(self):
        """
        Check if the graph is empty.
        :return: True, if the graph is empty; False, otherwise.
        """
        if len(self.dicN)==0:
            return True
        else:
            return False

    def numNodes(self):
        """
        Return the number of nodes.
        :return: the number of nodes.
        """
        return len(self.dicN)

    def numEdges(self):
        """
        Return the number of edges.
        :return: the number of edges.
        """
        c=0
        for i in self.dicE:
            for j in self.dicE[i]:
                c=c+1
        c=c/2
        return int(c)


    def addNode(self, elem):
        """
        Add a new node with the specified value.
        :param elem: the node value.
        :return: the create node.
        """
        node = Node(self.numId, elem)
        self.dicN[self.numId] = node
        self.dicE[self.numId] = {}
        self.numId += 1
        return node


    def deleteNode(self, nodeId):
        """
        Remove the specified node.
        :param nodeId: the node ID (integer).
        :return: void.
        """
        for key in self.dicE[nodeId]:
            del self.dicE[key][nodeId]
        del self.dicE[nodeId]
        self.dicN.pop(nodeId)
        return None


    def getNode(self, id):
        """
        Return the node, if exists.
        :param id: the node ID (integer).
        :return: the node, if exists; None, otherwise.
        """
        return self.dicN.get(id)

    def getNodes(self):
        """
        Return the list of nodes.
        :return: the list of nodes.
        """
        return self.dicN


    def insertEdge(self, tail, head, weight=None):
        """
        Add a new edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: the (optional) edge weight (floating-point).
        :return: the created edge, if created; None, otherwise.
        """
        if self.dicN.__contains__(tail) and self.dicN.__contains__(head) and tail != head:
            edge=Edge(tail,head)
            self.dicE[tail][head]=edge
            return edge
        else:
            return None

    def deleteEdge(self, tail, head):
        """
        Remove the specified edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: void.
        """
        del self.dicE[tail][head]
        del self.dicE[head][tail]

    def getEdge(self, tail, head):
        """
        Return the node, if exists.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: the edge, if exists; None, otherwise.
        """
        if self.dicE.__contains__(tail):
            if self.dicE[tail].__contains__(head):
                return self.dicE[tail][head]

    def getEdges(self):
        """
        Return the list of edges.
        :return: the list of edges.
        """
        return self.dicE

    def isAdj(self, tail, head):
        """
        Checks if two nodes ar adjacent.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: True, if the two nodes are adjacent; False, otherwise.
        """
        return self.dicE[tail].__contains__(head)==None

    def getAdj(self, nodeId):
        """
        Return all nodes adjacent to the one specified.
        :param nodeId: the node id.
        :return: the list of nodes adjacent to the one specified.
        """
        list=[]
        for edge in self.dicE[nodeId]:
            list.append(self.dicE[nodeId][edge].head)
        return list

    def deg(self, nodeId):
        """
        Return the node degree.
        :param nodeId: the node id.
        :return: the node degree.
        """
        return len(self.dicE[nodeId])

    def print1(self):
        """
        Print the graph.
        :return: void.
        """
        for n in self.dicE:
            list=[]
            for node in self.dicE[n]:
                list.append(str(n)+" -> " + str(node.__str__()))
            print(list)

if __name__ == "__main__":
    graph = Graph() #
