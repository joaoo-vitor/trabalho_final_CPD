class TernaryTrieNode:
    def __init__(self, char):
        self.char = char 
        self.id = None  # Marks the end of a word
        self.left = None
        self.middle = None
        self.right = None 


class TernaryTrie:
    def __init__(self):
        self.root = None

    def insert(self, word, id):
        """
        Inserts a word into the ternary trie, with the player id.
        """
        def _insert(node, word, index):
            char = word[index]

            if node is None:
                node = TernaryTrieNode(char)

            if char < node.char:
                node.left = _insert(node.left, word, index)
            elif char > node.char:
                node.right = _insert(node.right, word, index)
            else:
                # If is the last letter
                if index + 1 < len(word):
                    node.middle = _insert(node.middle, word, index + 1)
                else:
                    node.id = id
            return node

        # Starts insertion from the root counting from index zero
        self.root = _insert(self.root, word, 0)

    def search(self, prefix):
        """
        Searches for words by a prefix
        Returns a list of words that has the prefix.
        """
        def _search(node, prefix, index):
            if node is None:
                return []

            char = prefix[index]

            if char < node.char:
                return _search(node.left, prefix, index)
            elif char > node.char:
                return _search(node.right, prefix, index)
            else: 
                # If is the last letter 
                if index + 1 == len(prefix):
                    return self.traverse(node.middle)
                return _search(node.middle, prefix, index + 1)
            
        # Start search from the root of the tree and counting from zero.
        return _search(self.root, prefix, 0)

    def traverse(self, node):
        """
        Traverses the ternary trie starting from a given node and return a list of the words.
        """
        
        result = []
        def _traverse(node, prefix):
            if node is None:
                return

            # Traverse the left subtree
            _traverse(node.left, prefix)

            # Visit the current node
            # If has an id, append the current word on the traverse list
            if node.id:
                result.append(node.id)

            # Traverse the middle subtree
            _traverse(node.middle, prefix + node.char)

            # Traverse the right subtree
            _traverse(node.right, prefix)

        _traverse(node, "")
        return result
