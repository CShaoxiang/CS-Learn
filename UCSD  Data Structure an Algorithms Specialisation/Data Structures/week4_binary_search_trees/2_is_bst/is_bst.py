#!/usr/bin/python3
import random
import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**28)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
  # Implement correct algorithm here
  # tree as array , root at index 0 , tree[0] contains key at 0 , left child at 1 , right child at 2
  if len(tree) == 0 :
     return True 
  else:
    return check_node_bst(tree,0 ,float('-inf') , float('inf'))

def check_node_bst(tree,node, min_value , max_value):
   # Base case , if no node , it is bst 
   if node == -1 :
      return True
   

   if tree[node][0] < min_value or tree[node][0] > max_value:
      return False
   
   # check 
   return check_node_bst(tree,tree[node][1],min_value,tree[node][0] -1 ) and check_node_bst(tree,tree[node][2],tree[node][0] +1,max_value)

# def generate_stress_test(num_nodes):
#     """
#     Generate a stress test input for the BST verification program.

#     :param num_nodes: Number of nodes in the tree (0 ≤ num_nodes ≤ 10^5).
#     :return: A string representing the input for the program.
#     """
#     if num_nodes == 0:
#         return "0\n"  # Empty tree case

#     # Generate a binary search tree
#     nodes = []
#     keys = list(range(1, num_nodes + 1))  # Unique keys for simplicity
#     random.shuffle(keys)  # Shuffle keys to create random BST structure

#     # Build a valid BST structure
#     for i in range(num_nodes):
#         left = 2 * i + 1 if 2 * i + 1 < num_nodes else -1
#         right = 2 * i + 2 if 2 * i + 2 < num_nodes else -1
#         nodes.append((keys[i], left, right))

#     # Format the result as the input format
#     result = f"{num_nodes}\n"
#     for key, left, right in nodes:
#         result += f"{key} {left} {right}\n"

#     return result


def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()

