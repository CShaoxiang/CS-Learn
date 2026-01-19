# python3
import sys

class SuffixTree:
    def __init__(self, text):
       
        self.tree = {0: {}}  # Root node, represented as a dictionary
        self.node_count = 0  # To assign unique IDs to nodes
        self.build_suffix_tree(text)

    def build_suffix_tree(self,text):
        """
        Construct the suffix tree from the given text.
        """
        for i in range(len(text)):
            current_node = 0  # Start at the root node
            suffix = text[i:]  # Current suffix to insert
            j = 0  # Position in the suffix

            while j < len(suffix):
                char = suffix[j]

                # Check if there's an edge labeled with this character
                if char in self.tree[current_node]:
                    edge, next_node = self.tree[current_node][char]
                    # Find the longest match between the edge and the suffix
                    k = 0
                    while k < len(edge) and j + k < len(suffix) and edge[k] == suffix[j + k]:
                        k += 1

                    # Case 1: Exact match (continue to next node)
                    if k == len(edge):
                        current_node = next_node
                        j += k
                    else:
                        # Case 2: Split the edge
                        split_node = self.new_node()
                        self.tree[current_node][char] = (edge[:k], split_node)
                        self.tree[split_node] = {edge[k]: (edge[k:], next_node)}
                        self.tree[split_node][suffix[j + k]] = (suffix[j + k:], self.new_node())
                        break
                else:
                    # Case 3: No matching edge, create a new one
                    self.tree[current_node][char] = (suffix[j:], self.new_node())
                    break

    def new_node(self):
        """
        Create a new node and return its ID.
        """
        self.node_count += 1
        self.tree[self.node_count] = {}
        return self.node_count

    def get_edge_labels(self):
        """
        Collect all edge labels from the tree.
        """
        labels = []
        for node in self.tree:
            for char, (label, next_node) in self.tree[node].items():
                labels.append(label)
        return labels


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges.
    """
    suffix_tree = SuffixTree(text)
    return suffix_tree.get_edge_labels()

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))