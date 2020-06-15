## Data Structures Class
## Graphs DFS, BFS
## Binary trees - inorder, preorder, postorder
## Ricardo A. Calix, Ph.D.
################################################################################

import numpy as np
import collections
from collections import deque ## generalization of queue and stack or double ended queue

################################################################################

class GraphsClass():

    def __init__(self):
        self.graph = {}
        
    ##############################################################
        
    def graph_dfs(self, node, visited):
        if node not in visited:
            visited.append(node)
            for n in self.graph[node]:
                self.graph_dfs(n, visited)
        return visited
    
    ##############################################################
                    
    def graph_bfs(self, s):
          seen = [s]
          queue = collections.deque(  [s]   )
          while queue:
              vertex = queue.popleft()
              print(vertex)
              for node in self.graph[vertex]:
                  if node not in seen:
                      seen.append(node)
                      queue.append(node)
                      
                      
####################################################################
            
class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val
        
####################################################################

class BinaryTree():

    def __init__(self):
        self.root = None
        self.dict_add_vertical = {}
        
    ################################################################
 
    def traverse_bfs(self, node):
        seen = [node.data]
        queue = collections.deque(  [node]   )
        while queue:
            children = []
            vertex = queue.popleft()
            #print(vertex)
            if vertex.left:
                children.append(vertex.left)
            if vertex.right:
                children.append(vertex.right)
            for node in children:
                if node.data not in seen:
                    seen.append(node.data)
                    queue.append(node)
        return seen
 
    #################################################################
    ## this is the general dfs
    
    def traverse_preorder(self, node, list_nodes):
        list_nodes.append(node.data)
        if node.left:
            self.traverse_preorder(node.left, list_nodes)
        if node.right:
            self.traverse_preorder(node.right, list_nodes)
        return list_nodes
            
    ##################################################################
   
    def traverse_inorder(self, node, list_nodes):
        if node.left:
            self.traverse_inorder(node.left, list_nodes)
        list_nodes.append(node.data)
        if node.right:
            self.traverse_inorder(node.right, list_nodes)
        return list_nodes
        
    ##################################################################
    
    def traverse_postorder(self, node, list_nodes):
        if node.left:
            self.traverse_postorder(node.left, list_nodes)
        if node.right:
            self.traverse_postorder(node.right, list_nodes)
        list_nodes.append(node.data)
        return list_nodes
        
    ##################################################################
    
    def add_vertical_traverse(self, i, node):
        if i in self.dict_add_vertical.keys():
            self.dict_add_vertical[i] = self.dict_add_vertical[i] + node.data
        else:
            self.dict_add_vertical[i] = node.data
        if node.left:
            x = i - 1
            self.add_vertical_traverse(x, node.left)
        if node.right:
            x = i + 1
            self.add_vertical_traverse(x, node.right)
    
    ##################################################################
  
    
    




