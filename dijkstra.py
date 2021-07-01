"""
This is the implementation of the Dikstra Algorithm, based on two classes:
adjacency graph and priority queue.
"""
import numpy as np
from priority_queue import PriorityQueue

def init_for_dijkstra(graph, source_node_index):
    """
    Initialize a graph with a source_node_index to prepare for the dijkstra algorithm
    """
    distance_list = [np.inf] * graph.number_nodes
    distance_list[source_node_index] = 0
    predecessor_list = [np.inf] * graph.number_nodes
    predecessor_list[source_node_index] = None
    distance_queue = PriorityQueue(graph.index_list.copy(), distance_list.copy())
    return distance_list, predecessor_list, distance_queue
    
def dijkstra(graph, source_node_index):
    """
    This is an implementation of the Dijkstra algorithm. Input = a graph + source_node_index.
    Outputs = a list of distances + a list of predecessors
    """
    distance_list, predecessor_list, distance_queue = init_for_dijkstra(graph, source_node_index)
    while distance_queue.check_if_empty() is False:
        index_u = distance_queue.extract_lowest_distance()
        for index_v in graph.query_all_out_neighbors(index_u):
            if distance_list[index_u] + graph.adjacency_matrix[index_u, index_v] < distance_list[index_v]:
                distance_list[index_v] = \
                        distance_list[index_u] + graph.adjacency_matrix[index_u, index_v]
                predecessor_list[index_v] = index_u
                distance_queue.update_distance(index_v, distance_list[index_v])
    return distance_list, predecessor_list
