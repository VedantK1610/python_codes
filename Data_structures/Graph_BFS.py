from collections import defaultdict

class Graph:
    def __init__(self):
        #to store graph
        self.graph=defaultdict(list)

    def add_edge(self,a,b):
        self.graph[a].append(b)

    def bfs(self,root):
        visited=[False]*(max(self.graph)+1)
        queue=[]
        queue.append(root)
        visited[root]=True

        while queue:
            root=queue.pop(0)
            print(root,end=' ')

            for i in self.graph[root]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True

    def print(self):
        print(max(self.graph))

g=Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.print()

g.bfs(2)