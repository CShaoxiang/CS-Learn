# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):
        # Initialize children list
        self.children = [[] for _ in range(self.n)]
        for child_index in range(self.n):
            parent_index = self.parent[child_index]
            if parent_index != -1:
                self.children[parent_index].append(child_index)
            else:
                self.root = child_index

        # Use DFS to compute height
        return self._dfs(self.root)

    def _dfs(self, node):
        if not self.children[node]:  # If leaf node
            return 1
        max_child_height = 0
        for child in self.children[node]:
            child_height = self._dfs(child)
            max_child_height = max(max_child_height, child_height)
        return max_child_height + 1
def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
