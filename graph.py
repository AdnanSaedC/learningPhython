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

    def BFS(self, source):
        visited = {}
        for vertex in self.adjacencyList.keys():
            visited[vertex] = False
    
        queue = deque([source])
        visited[source] = True
    
        while queue:
            node = queue.popleft()
            print(" ",node, end=" -> ")
    
            for vertex in self.adjacencyList[node]:
                if not visited[vertex]:
                    visited[vertex] = True
                    queue.append(vertex)
                    
    def DFS(self, source):
        visited = {}
        stack = [source]
    
        for vertex in self.adjacencyList.keys():
            visited[vertex] = False
    
        while stack:
            vertex = stack.pop()
    
            if not visited[vertex]:
                visited[vertex] = True
                print(" ",vertex, end=" -> ")
    
                for adjacentNode in self.adjacencyList[vertex]:
                    if not visited[adjacentNode]:
                        stack.append(adjacentNode)


g=Graph()
g.addVertex(1,2)
g.addVertex(1,4)
g.addVertex(2,3)
g.addVertex(2,4)
g.addVertex(4,3)
g.addVertex(4,5)
g.addVertex(3,5)

g.printGraph()