from collections import defaultdict 
from collections import deque, namedtuple
class Graph: 
    def __init__(self): 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def bfs(self,node):
        visited = [False]*7
        queue = []
        
        queue.append(node)
        visited[node] = True
        print(queue)
        
        while queue:
            print("in here")
            node = queue.pop(0)
            print("Node:",node)
            for vertex in self.graph[node]:
                if visited[vertex]==False:
                    queue.append(vertex)
                    visited[vertex]=True
    


g = Graph() 
g.addEdge(1, 2) 
g.addEdge(1, 3) 
g.addEdge(2, 1) 
g.addEdge(2, 5)
g.addEdge(2, 4)
g.addEdge(3, 1)
g.addEdge(3, 5)
g.addEdge(4, 2)
g.addEdge(4, 5)
g.addEdge(4, 6)
g.addEdge(5, 2)
g.addEdge(5, 3)
g.addEdge(5, 6)
g.addEdge(5, 4) 
g.addEdge(6, 4)
g.addEdge(6, 5) 
print(g.graph)
# print ("Following is Breadth First Traversal (starting from vertex 2)") 
g.bfs(1) 
