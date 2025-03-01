# count substring using trie


class Trie:
    def __init__(self):
        self.links = [None] * 26

    def has_letter(self, letter):
        return self.links[Trie.getindex(letter)] is not None

    def insert(self, letter, val):
        self.links[Trie.getindex(letter)] = val

    @staticmethod
    def getindex(letter):
        return ord(letter)-ord('a')


def countDistinctSubstrings(s):
    t = Trie()

    count = 0

    for start_index, _ in enumerate(s):
        current = t
        for end_index in range(start_index, len(s)):
            letter = s[end_index]
            if not current.has_letter(letter):
                count += 1
                current.insert(letter, Trie())

            current = current.links[Trie.getindex(letter)]

    return count + 1 # 1 for empty string


if __name__ == '__main__':
    print(countDistinctSubstrings("abab"))
