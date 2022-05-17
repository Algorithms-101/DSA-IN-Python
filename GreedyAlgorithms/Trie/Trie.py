# Create Class
class TrieNodes:
    # Initialize
    def __init__(self, char):

        self.char = char
        self.is_end = False
        self.counter = 0
        self.children = {}

# Inherit Class and represent as an object
class Trie(object):

    # Instantiate method
    def __init__(self):
        self.root = TrieNodes("")
    
    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root
       
        for char in word:
            # If character is found create a new nodd
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNodes(char)
                node.children[char] = new_node
                node = new_node
        
        node.is_end = True

        # Increment Counter
        node.counter += 1
        
    def dfs(self, node, prefix):
   
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char)
        
    def query(self, x):
       
        self.output = []
        node = self.root
        
        # Check if a prefix is contained in a trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        
        # Implement Transversal method on Tree
        self.dfs(node, x[:-1])

        # Sort the result
        return sorted(self.output, key=lambda x: x[1], reverse=True)