class Graph:
    
    def __init__(self, vertexNumber):
        self.adjMatrix = [[-1]*vertexNumber for _ in range(vertexNumber)]
        self.vertex_number = vertexNumber
        self.verteces = {}
        self.verteces_list = [0]*vertexNumber
    
    def set_vertex(self, vertex, id):
        # check for safety
        if 0 <= vertex <= self.vertex_number:
            self.verteces[id] = vertex # ['a': 0, 'b': 1, ...]
            self.verteces_list[vertex] = id # ['a', 'b', 'c', ...]
    
    def set_edge(self, frm, to, cost=0):
        frm = self.verteces[frm]
        to = self.verteces[to]
        self.adjMatrix[frm][to] = cost
        # for undirected graph
        self.adjMatrix[to][frm] = cost

    def get_vertex(self):
        return self.verteces_list
    
    def get_edges(self):
        edges = []
        for i in range(self.vertex_number):
            for j in range(self.vertex_number):
                if self.adjMatrix[i][j] != -1:
                    edges.append((self.verteces_list[i], self.verteces_list[j], self.adjMatrix[i][j]))
        return edges
    
    def get_matrix(self):
        return self.adjMatrix

if __name__ == "__main__":
    G =Graph(6)
    G.set_vertex(0,'a')
    G.set_vertex(1,'b')
    G.set_vertex(2,'c')
    G.set_vertex(3,'d')
    G.set_vertex(4,'e')
    G.set_vertex(5,'f')
    G.set_edge('a','e',10)
    G.set_edge('a','c',20)
    G.set_edge('c','b',30)
    G.set_edge('b','e',40)
    G.set_edge('e','d',50)
    G.set_edge('f','e',60)
    print("Vertices of Graph")
    print(G.get_vertex())
    print("Edges of Graph")
    print(G.get_edges())
    print("Adjacency Matrix of Graph")
    print(G.get_matrix())