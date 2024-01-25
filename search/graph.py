import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        if start not in list(self.graph):
            return None # Handles edge case of start not being in the graph
        q = [] # A queue to maintain the order of nodes to be visited.
        visited = [] # Nodes visited (ordered inherently due to this being a list, but doesn't have to be)
        parent = {start: None} # Keeps track of the parent of each node (None for the root). This will help back-trace from "end" to "start" to find the shortest path
        q.append(start)
        visited.append(start)
        while len(q) > 0: # While there are 1+ nodes to be visited:
            v = q.pop(0) # First node to be visited
            N = self.graph[v]
            for w in N:
                if w not in visited:
                    visited.append(w)
                    q.append(w)
                    parent[w] = v
        if end == None:
            return visited
        elif end not in visited:
            return None
        else:
            # Trace back our steps from end to start using "parent"
            path = []
            current = end
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse() # "path" is currently from "end" to "start", so we should reverse it.
            return path
    def get_nodes(self):
        return list(self.graph)
    def get_all_possible_shortest_paths_nx(self, source, target):
        return list(nx.all_shortest_paths(self.graph, source = source, target = target))




