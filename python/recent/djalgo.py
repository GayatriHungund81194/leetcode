from collections import defaultdict 
from collections import deque, namedtuple
import numpy as np
class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 
        self.visited = [False]*5
        sef.visited[0] = True
        self.distances = [0]*5

    def addEdge(self,u,v,w): 
        self.graph[u].append((v,w))
    
    def shortestpath(self,start):
        node = start
        for i in range(len(self.distances)-1):
            self.visited[node] = True
            for vertex in self.graph[node]:
                dist1 = self.distances[node]
                dist2 = vertex[1]
                # print(self.distances[vertex[0]])
                # print(dist1+dist2)
                if (self.distances[vertex[0]] < (dist1 + dist2)):
                    self.distances[vertex[0]] = (dist1 + dist2)
            for j in range(len(self.visited)):
                if (self.visited[i]==False and ):






g = Graph()
g.addEdge(1,2,3)
g.addEdge(1,3,4)
g.addEdge(2,3,0.5)
g.addEdge(3,4,1)
g.shortestpath(1)
print(g.visited)
print(g.distances)


