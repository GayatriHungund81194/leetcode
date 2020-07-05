import sys 

class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 

    def printSolution(self, dist): 
        print ("Vertex tDistance from Source") 
        for node in range(self.V): 
            print (node, "t", dist[node])

    def mindist(self,dist,visitedSet):
        min = sys.maxsize 
        for v in range(self.V): 
            if dist[v] < min and visitedSet[v] == False: 
                min = dist[v] 
                min_index = v 
        return min_index

    def shortestpath(self,src):
        dist = [sys.maxsize] * self.V
        print("Dist",dist)
        dist[src] = 0
        visitedSet = [False] * self.V 
        for cout in range(self.V): 
            u = self.mindist(dist, visitedSet)
            print(u)
            visitedSet[u] = True
            




g = Graph(3) 
g.graph = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
g.shortestpath(0)

