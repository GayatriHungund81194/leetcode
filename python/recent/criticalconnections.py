from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.visited = [0]*5

    def addEdge(self,key,value):
        self.graph[key].append(value)
        
    def dfs(self,start,graph):
        dfsStack = list()
        dfsStack.append(start)
        while dfsStack:
            elem = dfsStack[-1]
            dfsStack.pop()
            print(elem)
            if (self.visited[elem]==0):
                self.visited[elem] = 1
            for node in graph[elem]:
                if (not self.visited[node]):
                    dfsStack.append(node)
    
    def checkCritical(self):
        print(self.graph)
        l = self.graph
        print(self.graph)





g = Graph()
g.addEdge(1, 0);  
g.addEdge(0, 2);  
g.addEdge(2, 1);  
g.addEdge(0, 3);  
g.addEdge(1, 4);  

print(g.graph)
g.checkCritical()