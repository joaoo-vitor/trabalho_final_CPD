class TernaryTrieNode:
    def __init__(self, char):
        self.char = char  # Character stored in this node
        self.is_end_of_word = False  # Marks the end of a word
        self.left = None  # Left child (characters less than this char)
        self.middle = None  # Middle child (characters equal to this char)
        self.right = None  # Right child (characters greater than this char)


class TernaryTrie:
    def __init__(self):
        self.root = None

    def insert(self, word):
        """
        Inserts a word into the ternary trie.
        """
        def _insert(node, word, index):
            char = word[index]

            if node is None:
                node = TernaryTrieNode(char)

            if char < node.char:
                node.left = _insert(node.left, word, index)
            elif char > node.char:
                node.right = _insert(node.right, word, index)
            else:  # char == node.char
                if index + 1 < len(word):
                    node.middle = _insert(node.middle, word, index + 1)
                else:
                    node.is_end_of_word = True

            return node

        self.root = _insert(self.root, word, 0)

    def search(self, word):
        """
        Searches for a word in the ternary trie.
        Returns True if the word exists, False otherwise.
        """
        def _search(node, word, index):
            if node is None:
                return False

            char = word[index]

            if char < node.char:
                return _search(node.left, word, index)
            elif char > node.char:
                return _search(node.right, word, index)
            else:  # char == node.char
                if index + 1 == len(word):
                    return node.is_end_of_word
                return _search(node.middle, word, index + 1)

        return _search(self.root, word, 0)

    def traverse(self):
        """
        Traverses the ternary trie and prints all the words.
        """
        result = []

        def _traverse(node, prefix):
            if node is None:
                return

            # Traverse the left subtree
            _traverse(node.left, prefix)

            # Visit the current node
            if node.is_end_of_word:
                result.append(prefix + node.char)

            # Traverse the middle subtree
            _traverse(node.middle, prefix + node.char)

            # Traverse the right subtree
            _traverse(node.right, prefix)

        _traverse(self.root, "")
        return result


# Example usage:
trie = TernaryTrie()
trie.insert("cat")
trie.insert("car")
trie.insert("bat")
trie.insert("bar")
trie.insert("can")

print("Words in the trie:", trie.traverse())
print("Search for 'cat':", trie.search("cat"))
print("Search for 'cap':", trie.search("cap"))
