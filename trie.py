from typing import Dict, List


class Node:
    def __init__(self):
        Char = str
        self.children: Dict[Char, Node] = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word: str):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = Node()
            current = current.children[char]
        current.is_word = True
        return self

    def contains(self, word: str):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        print(current.is_word)
        return True

    def search(self, word: str):
        current = self.root
        ancestors: List[str] = []
        for char in word:
            if char not in current.children:
                return []  # not found
            current = current.children[char]
            ancestors.append(char)
        result: List[str] = []
        self.dfs(current, ancestors, result)
        return result

    def dfs(self, node: Node, ancestors: List[str], result: List[str]):
        for char in node.children:
            ancestors.append(char)
            if node.children[char].is_word:
                result.append("".join(ancestors))
            self.dfs(node.children[char], ancestors, result)
            ancestors.pop()
