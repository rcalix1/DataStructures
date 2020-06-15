## Data structure problems
###########################################################

import numpy as np
import collections
from collections import deque ## generalization of queue and stack or double ended queue

###########################################################

from DataStructuresClass import GraphsClass
from DataStructuresClass import Node
from DataStructuresClass import BinaryTree

##########################################################


graph1 = GraphsClass()

graph1.graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}


visited = graph1.graph_dfs('F', [])
print(visited)
print("*********************")

#######################################################


graph2 = GraphsClass()

graph2.graph = {
                 "a" : set(["b","c"]),
                 "b" : set(["a", "d"]),
                 "c" : set(["a", "d"]),
                 "d" : set(["e"]),
                 "e" : set(["a"])
                }


graph2.graph_bfs("a")
print("*********************")

#######################################################


deque1 = deque('ghi')                 # make a new deque with three items

for elem in deque1:
    print(elem.upper())

deque1.append('j')                    # add a new entry to the right side
deque1.appendleft('f')                # add a new entry to the left side

print(deque1)
print( deque1.pop() )                         # return and remove the rightmost item
print(  deque1.popleft()  )                    # return and remove the leftmost item

print(deque1)

print(deque1[0])                             # peek at leftmost item
print(deque1[-1]  )                          # peek at rightmost item


######################################################

node = Node(50)

tree2 = BinaryTree()
tree2.root = node

tree2.root.left = Node(25)
tree2.root.right = Node(75)
tree2.root.left.left = Node(3)
tree2.root.left.right = Node(42)
tree2.root.right.left = Node(60)
tree2.root.right.right = Node(120)

l = tree2.traverse_preorder(tree2.root, [])
print(l)

## [50, 25, 3, 42, 75, 60, 120] ## preorder
######################################################

node = Node(50)

tree3 = BinaryTree()
tree3.root = node

tree3.root.left = Node(25)
tree3.root.right = Node(75)
tree3.root.left.left = Node(3)
tree3.root.left.right = Node(42)
tree3.root.right.left = Node(60)
tree3.root.right.right = Node(120)

l = tree3.traverse_inorder(tree3.root, [])
print(l)

## [3, 25, 42, 50, 60, 75, 120]  ## inorder
######################################################

node = Node(50)

tree4 = BinaryTree()
tree4.root = node

tree4.root.left = Node(25)
tree4.root.right = Node(75)
tree4.root.left.left = Node(3)
tree4.root.left.right = Node(42)
tree4.root.right.left = Node(60)
tree4.root.right.right = Node(120)

l = tree4.traverse_postorder(tree4.root, [])
print(l)

## [3, 42, 25, 60, 120, 75, 50] ## post order
######################################################


node = Node(50)

tree5 = BinaryTree()
tree5.root = node

tree5.root.left = Node(25)
tree5.root.right = Node(75)
tree5.root.left.left = Node(3)
tree5.root.left.right = Node(42)
tree5.root.right.left = Node(60)
tree5.root.right.right = Node(120)

l = tree5.traverse_bfs(tree5.root)
print(l)

## [50, 25, 75, 3, 42, 60, 120]  ## bfs
######################################################

node = Node(50)

tree6 = BinaryTree()
tree6.root = node

tree6.root.left = Node(25)
tree6.root.right = Node(75)
tree6.root.left.left = Node(3)
tree6.root.left.right = Node(42)
tree6.root.right.left = Node(60)
tree6.root.right.right = Node(120)

tree6.root.left.left.right = Node(7)
tree6.root.right.left.right = Node(6)

tree6.add_vertical_traverse(0, tree6.root)
print(tree6.dict_add_vertical)

######################################################

print("<<<<<<<<<<<<<<<<<<<<DONE>>>>>>>>>>>>>>>>>>>>>")



