#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
    Graph implementation based on adjacency matrix
"""

import numpy as np

class Node:
    """
        Class for nodes. Can hold a label that is display in visualization
        + an index for the matrix
    """
    def __init__(self, index = 0, label="Default node"):
        self.label = label
        self.index = index


class Edge:
    """
        Class for edges. Can have a label, weight and a direction
    """
    def __init__(self, start_node_index, end_node_index, weight=1):
        self.start_node_index = start_node_index
        self.end_node_index = end_node_index
        self.weight = weight


class GraphAdjacency:
    """
        Weighted, directed graph that supports the operations that
        are necessary for Dijkstra's algorithm
    """
    def __init__(self, node_list, edge_list=None):
        """Constructor that takes a node list and an edge list as input"""
        self.node_list, self.edge_list = node_list, edge_list
        self.number_nodes, index_list = len(self.node_list), []
        for node in self.node_list:
            index_list.append(node.index)
        self.index_list = index_list
        adjacency_matrix = np.full((self.number_nodes, self.number_nodes), None)
        for j in self.index_list:
            adjacency_matrix[j,j] = 0
        for i in self.edge_list:
            adjacency_matrix[i.start_node_index, i.end_node_index] =  i.weight
        self.adjacency_matrix = adjacency_matrix
   
    def query_all_out_neighbors(self, node_index):
        """
            Returns a list of indices of all nodes
            which are adjacent to the input node via an outgoing edge
        """
        list_index_out_neighbours = []
        if node_index in self.index_list:
            list_index_except_node_index = self.index_list.copy()
            list_index_except_node_index.remove(node_index)
            for an_index in list_index_except_node_index:
                adjacency_matrix_entry = self.adjacency_matrix[node_index, an_index]
                if adjacency_matrix_entry is not None and adjacency_matrix_entry >= 0:
                    list_index_out_neighbours.append(an_index)
        return list_index_out_neighbours
