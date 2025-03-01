# a implementation of trie (leetcode 208)
#@AryanERTash


class Trie:

    def __init__(self):
        """
            self.links: point to next links
            self.isword: whether the given node indicated end of a word
        """
        self.links = [None] * 26        
        self.isword = False
        

    def insert(self, word: str) -> None:
        """
        Insert into Trie

        Args:
            word (str): The word to insert in Trie
        """
        current = self

        for letter in word:
            index = ord(letter) - ord('a') # or % 26

            if current.links[index] is None:
                current.links[index] = Trie()
            current = current.links[index]
        

        current.isword = True
        

    def search(self, word: str) -> bool:

        """
        Search for a word in trie

        Returns:
            bool: return whether the given word is present or not
            
        """

        current = self

        for letter in word:
            index = ord(letter) - ord('a')
            if current.links[index] is None:
                return False
            current = current.links[index]
        

        return current.isword
        

    def startsWith(self, prefix: str) -> bool:

        current = self

        for letter in prefix:
            index = ord(letter) - ord('a')
            if current.links[index] is None:
                return False
            current = current.links[index]
        
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)