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
    assert len(G.bfs("31806696")) == 30 # test case to ensure all 30 nodes are traversed in the BFS in the subgraph
    assert G.bfs("31806696", end = "fake_node") is None # test case to ensure "None" is returned when the end node is not in the graph
    assert G.bfs("fake_node") is None # test case to ensure "None" is returned when the start node is not in the graph
    empty = Graph(filename = "data/empty.adjlist")
    assert empty.bfs("fake_node") is None # test case to ensure "None" is returned for a bfs in an empty graph

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
    print(len(G.get_nodes())) # Get all the nodes in the full citation network graph
    print(len(G.bfs("34916529"))) # This is the first node in the node list printed in the previous line
    print(G.bfs("34916529")) # There is only one neighbor for the aforementioned node, so we know that not all nodes are reachable from this node
    assert G.bfs("34916529", end = "34858697") is None # Ensure that "34858697" (which is a random node that shouldn't be part of "34916529"'s network, is not reached (i.e. "None is returned"))
    
