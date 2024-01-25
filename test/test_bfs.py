# write tests for bfs
import pytest
from search.graph import Graph

class IncorrectBFSError(Exception):
    """
    Raised when the computed shortest path is incorrect, when compared to the Networkx ground truth
    """
    pass

class IncorrectGetNodesError(Exception):
    """
    Raised when the node list retrieved is incorrect for the given Graph object
    """
    pass

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    G = Graph(filename = "data/tiny_network.adjlist")
    assert len(G.bfs("31806696")) == 30, IncorrectBFSError("Number of nodes is not 30") # test case to ensure all 30 nodes are traversed in the BFS in the subgraph
    assert G.bfs("31806696", end = "fake_node") is None, IncorrectBFSError("Fake node should not be reachable") # test case to ensure "None" is returned when the end node is not in the graph
    assert G.bfs("fake_node") is None, IncorrectBFSError("Fake node does not exist in the graph") # test case to ensure "None" is returned when the start node is not in the graph
    empty = Graph(filename = "data/empty.adjlist")
    assert empty.bfs("fake_node") is None, IncorrectGetNodesError("Empty Graph should not have Fake Node") # test case to ensure "None" is returned for a bfs in an empty graph

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    G = Graph(filename = "data/citation_network.adjlist")
    #print(len(G.get_nodes())) # Get all the nodes in the full citation network graph
    #print(G.bfs("Franklin Huang", "David Quigley")) # This is the first node in the node list printed in the previous line
    #print(G.get_all_possible_shortest_paths_nx("Franklin Huang", "David Quigley"))
    #print(G.bfs("David Quigley", "Franklin Huang"))
    assert len(G.get_nodes()) == 5210, IncorrectBFSError("Number of nodes is not 5210")
    assert G.bfs("Franklin Huang", "David Quigley") in G.get_all_possible_shortest_paths_nx("Franklin Huang", "David Quigley"), IncorrectBFSError("Computed BFS from Franklin Huang to David Quigley is incorrect")
    assert G.bfs("Franklin Huang", "David Quigley") != G.bfs("David Quigley", "Franklin Huang"), IncorrectBFSError("BFS computed is incorrectly computed to be commutative between Franklin Huang and David Quigley")
    assert G.bfs("Franklin Huang", end = "PI_that_doesnt_exist") is None, IncorrectBFSError("PI_that_doesnt_exist should be unreachable from Franklin Huang") # Ensure that "PI_that_doesnt_exist" (which is a random node that shouldn't be part of "Franklin Huang"'s network, is not reached (i.e. "None is returned"))
    
