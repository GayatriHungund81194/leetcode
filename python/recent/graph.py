from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = [0]*6

    def addEdge(self,key,value):
        self.graph[key].append(value)

    def bfsAdjList(self,src):
        bfsqueue = list()

        bfsqueue.append(src)

        while len(bfsqueue) > 0:
            elem = bfsqueue.pop(0)
            self.visited[elem] = 1
            print(" ",elem)
            for i in range(len(self.graph[elem])):
                li = self.graph[elem]
                if (self.visited[li[i]] == 0):
                    bfsqueue.append(li[i])
                    self.visited[li[i]] = 1
    
    def bfsAdjMat(self,src,adjMat):
        bfsqueue = list()
        bfsqueue.append(src)

        while len(bfsqueue):
            elem = bfsqueue.pop(0)
            self.visited[elem] = 1
            print(" ",elem)
            adj = self.findAdj(elem,adjMat)
            for i in range(len(adj)):
                elem  = adj[i]
                if (self.visited[adj[i]] == 0):
                    bfsqueue.append(elem)
                    self.visited[elem] = 1

    def findAdj(self, elem, adjMat):
        adjVertices = list()
        for i in range(len(adjMat)):
            for j in range(len(adjMat[0])):
                if (adjMat[i][j]==1):
                    adjVertices.append(j)
        return adjVertices

    def dfs(self,source):
        dfsStack = list()
        dfsStack.append(source)
        while len(dfsStack):
            elem = dfsStack[-1]
            dfsStack.pop()
            print(elem)
            if (not self.visited[elem]):
                self.visited[elem] = 1
                #print(elem)
            
            for node in self.graph[elem]:
                if (not self.visited[node]):
                    dfsStack.append(node)

    


        
g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,0)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(2,0)
g.addEdge(2,1)
g.addEdge(2,4)
g.addEdge(3,1)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,2)
g.addEdge(4,3)
g.addEdge(4,5)
g.addEdge(5,3)
g.addEdge(5,4)
#print(g.graph)
#g.bfsAdjList(4)

adjMat = [[1,1,1,1,0],[1,1,1,1,0],[1,1,0,0,0],[0,0,0,0,0]]
# g.bfsAdjMat(0,adjMat)
g.dfs(0)