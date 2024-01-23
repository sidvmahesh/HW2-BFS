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
            return None
        q = []
        visited = []
        q.append(start)
        visited.append(start)
        while len(q) > 0:
            v = q.pop(0)
            N = self.graph[v]
            for w in N:
                if w not in visited:
                    visited.append(w)
                    q.append(w)
        if end == None:
            return visited
        elif end not in visited:
            return None
        else:
            return visited[:x.index(end)+1]
    def get_nodes(self):
        return list(self.graph)




