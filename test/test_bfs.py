# write tests for bfs
import pytest
from search.graph import Graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    G = Graph(filename = "data/tiny_network.adjlist")
    assert len(G.bfs("31806696")) == 30
    assert G.bfs("31806696", end = "fake_node") is None
    assert G.bfs("fake_node") is None
    empty = Graph(filename = "data/empty.adjlist")
    assert empty.bfs("fake_node") is None

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
    print(len(G.get_nodes()))
    print(len(G.bfs("34916529")))
    print(G.bfs("34916529"))
    assert G.bfs("34916529", end = "34858697") is None
    
