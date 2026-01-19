#!/usr/bin/python3
import random
import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

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

