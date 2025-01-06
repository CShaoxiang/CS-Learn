# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._inOrderTraversal(0)          
    return self.result

  def preOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._preOrderTraversal(0)
                
    return self.result

  def postOrder(self):
    self.result = []
    # Finish the implementation
    # You may need to add a new recursive method to do that
    self._postOrderTraversal(0)
    return self.result
  
  def _inOrderTraversal(self,node):
    if node == -1:
      return 
    
    self._inOrderTraversal(self.left[node])
    self.result.append(self.key[node])
    self._inOrderTraversal(self.right[node])

  def _preOrderTraversal(self, node):
        if node == -1:  # Base case: no node
            return
        # Visit current node, left subtree, then right subtree
        self.result.append(self.key[node])
        self._preOrderTraversal(self.left[node])
        self._preOrderTraversal(self.right[node])

  def _postOrderTraversal(self, node):
        if node == -1:  # Base case: no node
            return
        # Visit left subtree, right subtree, then current node
        self._postOrderTraversal(self.left[node])
        self._postOrderTraversal(self.right[node])
        self.result.append(self.key[node])
    


   

def main():
	tree = TreeOrders()
	tree.read()
	print(" ".join(str(x) for x in tree.inOrder()))
	print(" ".join(str(x) for x in tree.preOrder()))
	print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
