
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_terminal = False
        self.sofifa_ids = set()
       
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, sofifa_id, tag):
        current_node = self.root
        # Empty tags are ignored
        if(len(tag)):
            for character in tag:
                if character not in current_node.children:
                    current_node.children[character] = TrieNode()
                current_node = current_node.children[character]
            current_node.sofifa_ids.add(sofifa_id)
            current_node.is_terminal = True

    def search(self, prefix):
        current_node = self.root
        matching_ids = set()

        for character in prefix:
            if character in current_node.children:
                current_node = current_node.children[character]
            else:
                return list(matching_ids)

            if current_node.is_terminal:
                matching_ids.update(current_node.sofifa_ids)
         
        return list(matching_ids)

    def depth_first_search(self, node, current_prefix, result_ids):
        if node.is_terminal:
            result_ids.add(node.char)
        for character, child_node in node.children.items():
            new_prefix = current_prefix + character
            self.depth_first_search(child_node, new_prefix, result_ids)
