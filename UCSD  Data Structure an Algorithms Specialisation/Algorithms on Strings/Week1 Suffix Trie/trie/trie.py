# python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

class Trie:
    def __init__(self, patterns):
        self.nodes = {0: {}}  # Root node
        self.node_count = 0  # To assign unique IDs to nodes
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
        current_node_id = 0  # Start at root node

        for char in pattern:
            if char not in self.nodes[current_node_id]:
                # Create a new node
                self.node_count += 1
                self.nodes[current_node_id][char] = self.node_count
                self.nodes[self.node_count] = {}  # Initialize the new node

            # Move to the next node
            current_node_id = self.nodes[current_node_id][char]

    def print_trie(self):
        """
        Prints the trie in the required format.
        """
        for node_id, edges in self.nodes.items():
            for char, child_node_id in edges.items():
                print("{}->{}:{}".format(node_id, child_node_id, char))



def build_trie(patterns):
    """
    Build the trie structure from the given patterns.
    """
    trie = Trie(patterns)
    return trie


if __name__ == '__main__':
    # Read input patterns
    patterns = sys.stdin.read().split()[1:]
    trie = build_trie(patterns)

    # Print the trie in the required format
    trie.print_trie()
