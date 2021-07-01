#!/usr/bin/env python
# coding: utf-8

# In[2]:

"""Simple priority queue implementation based on a linked list"""

class PriorityQueue:
    """
    An implementation of the priority queue as a linked list
    """
    def __init__(self, index_list, distance_list):
        """
        Initialize a priority queue, from input index list and input distance list
        """
        if len(index_list) != len(distance_list):
            self.index_list = None
            self.distance_list = None
        else:
            self.index_list = index_list
            self.distance_list = distance_list
    def check_if_empty(self):
        """
        Check whether a priority queue is empty(return True)
        or non-empty(return False)
        """
        if len(self.index_list) == 0:
            print('Empty')
            return True
        print('Not Empty')
        return False
    def update_distance(self, index_to_insert, new_distance):
        """
        Update the distance if the input index exists in the priority queue
        """
        if index_to_insert in self.index_list:
            temp_index = self.index_list.index(index_to_insert)
            self.distance_list[temp_index ] = new_distance
    def extract_lowest_distance(self):
        """
        Extract the undex of the element with the lowest distance from a priority queue
        """
        lowest_distance = min(self.distance_list)
        temp_index = self.distance_list.index(lowest_distance)
        lowest_distance_index = self.index_list[temp_index]
        self.distance_list.remove(lowest_distance)
        self.index_list.remove(lowest_distance_index)
        return lowest_distance_index
