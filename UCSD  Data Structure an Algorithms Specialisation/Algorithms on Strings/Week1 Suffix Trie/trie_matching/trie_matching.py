# python3
import sys
class Trie:
    class Node:
        def __init__(self):
            self.children = {}
            self.is_end = False 

    def __init__(self, patterns):
        self.root = self.Node()
        self.construct_trie(patterns)

    def construct_trie(self, patterns):
        """
        Constructs the trie by inserting all patterns.
        """
        for pattern in patterns:
            self.insert(pattern)

    def insert(self, pattern):
        """
        Inserts a pattern into the trie.
        """
        current_node = self.root # Start at root node

        for char in pattern:
            if char not in current_node.children:
              
                current_node.children[char] = self.Node()  # Initialize the new node
            
            current_node = current_node.children[char]

        current_node.is_end = True

    def prefix_trie_matching(self,text):
        """
        Checks if any pattern in the trie matches a prefix of the text.
        """
        current_node = self.root

        for char in text:
            if char in current_node.children:
                current_node = current_node.children[char]

                if current_node.is_end:
                    return True
        return False
    
            
    


        
def solve(text, n, patterns):
    myTrie = Trie(patterns)

    result = []

    for i in range(len(text)): # O(T)
        current_node = myTrie.root
        j = i

        while j <len(text): # O()
            char = text[j]
            if char in current_node.children:
                current_node = current_node.children[char]
                if current_node.is_end :
                    result.append(i)
                    break
                j+=1
            
            else:
                break
    
       
    return sorted(result)



if __name__ == '__main__':
    # text = sys.stdin.readline().strip()
    # n = int(sys.stdin.readline().strip())
    # patterns = []
    # for i in range(n):
    #     patterns.append(sys.stdin.readline().strip())

    # ans = solve(text, n, patterns)

    # sys.stdout.write(' '.join(map(str, ans)) + '\n')
    txt = 'geeksforgeeks'
    print(txt[0:])