class Graph:

    def __init__(self):
        self.adjacencyList={}

    def addEdgesToTheGraph(self,edgeToBeAdded):
        if edgeToBeAdded not in self.adjacencyList:
            self.adjacencyList[edgeToBeAdded]=[]

    def addVertex(self,source,destination):
        # here we are writing this for undirected graph
        self.addEdgesToTheGraph(source)
        self.addEdgesToTheGraph(destination)

        # now adding vertexex
        self.adjacencyList[source].append(destination)
        self.adjacencyList[destination].append(source)

    def printGraph(self):
        for vertex in self.adjacencyList:
            print(vertex ," -> ",self.adjacencyList[vertex])


g=Graph()
g.addVertex(1,2)
g.addVertex(1,4)
g.addVertex(2,3)
g.addVertex(2,4)
g.addVertex(4,3)
g.addVertex(4,5)
g.addVertex(3,5)

g.printGraph()