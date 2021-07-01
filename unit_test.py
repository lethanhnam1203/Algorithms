#!/usr/bin/env python
# coding: utf-8

# In[6]:

import unittest
from graph import Node, Edge, GraphAdjacency
from priority_queue import PriorityQueue
import numpy as np

# In[7]:


class Test_Graph_Adjacency_Init(unittest.TestCase):
    def test_graph_init_with_multi_elements(self):
        node_list = [Node(0,"1"), Node(1,"1"), Node(2,"3"),
                     Node(3,"4"), Node(4,"5"), Node(5,"6")]
        edge_list = [Edge(0, 1, 2), Edge(0, 2, 1), Edge(1, 3, 2),
                     Edge(1, 4, 1), Edge(2, 3, 5), Edge(2, 4, 4),
                     Edge(3, 5, 1), Edge(4, 5, 0)]
        graph = GraphAdjacency(node_list, edge_list)  
        self.assertEqual(graph.number_nodes, 6)
        self.assertEqual(graph.adjacency_matrix[2,2], 0)
        self.assertEqual(graph.adjacency_matrix[0,1], 2)
        self.assertEqual(graph.adjacency_matrix[4,5], 0)
        self.assertEqual(graph.adjacency_matrix[2,4], 4)
        self.assertEqual(graph.adjacency_matrix[1,4], 1)
        self.assertEqual(graph.index_list[2], 2)
        self.assertIsNone(graph.adjacency_matrix[3,1])
        self.assertIsNone(graph.adjacency_matrix[4,3])
        self.assertIsNone(graph.adjacency_matrix[5,2])
        
    def test_graph_init_with_empty(self):  
        graph = GraphAdjacency([], [])
        self.assertEqual(graph.number_nodes, 0)
        self.assertEqual(np.shape(graph.adjacency_matrix), (0, 0))


class Test_Graph_Adjacency_Query_Out_Neighbours(unittest.TestCase):   
    def test_graph_query_out_neighbours(self):
        node_list = [Node(0,"1"), Node(1,"1"), Node(2,"3"),
                     Node(3,"4"), Node(4,"5"), Node(5,"6")]
        edge_list = [Edge(0, 1, 2), Edge(0, 2, 1), Edge(1, 3, 2),
                     Edge(1, 4, 1), Edge(2, 3, 5), Edge(2, 4, 4),
                     Edge(3, 5, 1), Edge(4, 5, 0)]
        graph = GraphAdjacency(node_list, edge_list) 
        self.assertEqual(graph.query_all_out_neighbors(0), [1, 2])
        self.assertEqual(graph.query_all_out_neighbors(4), [5])
        self.assertEqual(graph.query_all_out_neighbors(2), [3, 4])
        self.assertEqual(graph.query_all_out_neighbors(5), [])
        self.assertEqual(graph.query_all_out_neighbors(98), [])

        
class Test_Init_Priority_Queue(unittest.TestCase):
    def test_priority_queue_init_with_multi_elements(self):
        index_list = [0, 1, 2, 3, 4, 5, 8]
        distance_list = [0, 2, 1, 4, 3, 3,6]
        priority_queue = PriorityQueue(index_list, distance_list)
        self.assertEqual(priority_queue.index_list, [0, 1, 2, 3, 4, 5, 8])
        self.assertEqual(priority_queue.distance_list, [0, 2, 1, 4, 3, 3, 6])
    
    def test_false_priority_queue_init(self):
        index_list_false = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        distance_list_false = [0, 2, 1, 4, 3, 3]
        priority_queue_false = PriorityQueue(index_list_false, distance_list_false)
        self.assertIsNone(priority_queue_false.index_list)
        self.assertIsNone(priority_queue_false.distance_list)

        
class Test_Check_If_Priority_Queue_Is_Empty(unittest.TestCase):
    def test_check_priority_queue_empty(self):
        empty_priority_queue = PriorityQueue([], [])
        self.assertTrue(empty_priority_queue.check_if_empty())
        
    def test_check_priority_queue_not_empty(self):
        index_list = [0, 1, 2, 3, 4, 5]
        distance_list = [0, 340, 143, 324, 312, 354]
        priority_queue = PriorityQueue(index_list, distance_list)
        self.assertFalse(priority_queue.check_if_empty())

        
class Test_Extract_Lowest_Distance_From_Priority_Queue(unittest.TestCase):
    def test_extract_lowest_distance_one(self):
        index_list_one = [20, 11, 24, 3, 7, 5]
        distance_list_one = [10, 3, 999, 1, 6, 7]
        priority_queue_one = PriorityQueue(index_list_one, distance_list_one)
        self.assertEqual(priority_queue_one.extract_lowest_distance(), 3)

    def test_extract_lowest_distance_two(self):
        index_list_two = [0, 1, 2, 3, 4, 5]
        distance_list_two = [0, 3, 1003030, 94949, 54, 222222222]
        priority_queue_two = PriorityQueue(index_list_two, distance_list_two)
        self.assertEqual(priority_queue_two.extract_lowest_distance(), 0)

        
class Update_Distance_Priority_Queue(unittest.TestCase):
    def setUp(self):
        index_list = [0, 1, 2, 3, 4, 5]
        distance_list = [0, 2, 1, 4, 300, 3]
        self.priority_queue = PriorityQueue(index_list, distance_list)

    def test_update_distance_impossible(self):
        self.priority_queue.update_distance(9,70)
        self.assertEqual(self.priority_queue.distance_list, [0, 2, 1, 4, 300, 3])

    def test_update_distance_possible(self):
        self.priority_queue.update_distance(4,45)
        self.assertEqual(self.priority_queue.distance_list, [0, 2, 1, 4, 45, 3])

        
if __name__ == "__main__":
    unittest.main()


# In[ ]:




