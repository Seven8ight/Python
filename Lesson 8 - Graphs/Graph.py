class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __repr__(self):
        graph_str = ""

        for node, neighbors in self.adj_list.items():
            graph_str += f"{node} -> {neighbors}\n"

        return graph_str
    
    def add_node(self,node):
        if node not in self.adj_list.keys():
            self.adj_list[node] = set()
        else:
            raise ValueError("Node exists already")

    def remove_node(self,node):
        if node not in self.adj_list.keys():
            raise ValueError("Node does not exist")
        
        for neighbors in self.adj_list.values():
            neighbors.discard(node)

        del self.adj_list[node]

    def add_edge(self,from_node,to_node,weight=None):
        if from_node not in self.adj_list:
            self.add_node(from_node)

        if to_node not in self.adj_list:
            self.add_node(to_node)

        if weight is None:
            self.adj_list[from_node].add(to_node)
            
            if not self.directed:
                self.adj_list[to_node].add(from_node)
        else:
            self.adj_list[from_node].add(to_node,weight)
            
            if not self.directed:
                self.adj_list[from_node].add((from_node,weight))

    def remove_edge(self,from_node,to_node):
        if from_node in self.adj_list:
            if to_node in self.adj_list[from_node]:
                self.adj_list[from_node].remove(to_node)
            else:
                raise ValueError("Edge does not exist")
            
            if not self.directed:
                if from_node in self.adj_list[to_node]:
                    self.adj_list[to_node].remove(from_node)
        else:
            raise ValueError("Edge does not exists")

    def get_neighbors(self,node):
        return self.adj_list.get(node,set())

    def has_node(self,node):
        return node in self.adj_list

    def has_edge(self,from_node,to_node):
        if from_node in self.adj_list:
            return to_node in self.adj_list[from_node]
        return False
        
    def get_nodes(self):
        return list(self.adj_list.keys())

    def get_edges(self):
        edges=[]
        for from_node, neighbors in self.adj_list.items():
            for to_node in neighbors:
                edges.append((from_node,to_node))

    def BFS(self,start):
        visited = set()
        queue = [start]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)

                for neighbor in neighbors:
                    if isinstance(neighbor,tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        queue.append(neighbor)

        return order
    
    def DFS(self,start):
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_neighbors(node)

                for neighbor in sorted(neighbors,reverse=True):
                    if isinstance(neighbor,tuple):
                        neighbor = neighbor[0]
                    if neighbor not in visited:
                        stack.append(neighbor)

        return order
    
graph = Graph()

graph.add_node(12)
graph.add_node(13)
graph.add_node(14)
graph.add_node(15)
graph.add_edge(12,13)
graph.add_edge(13,14)
graph.add_edge(14,15)
graph.add_edge(12,15)
graph.add_node(16)

print(graph)

print(graph.BFS(14))
print(graph.DFS(12))