from sys import *
from collections import *
from math import *

from typing import *


class Trie:
    def __init__(self):
        self.links = [None] * 26
        self.isword = False

    def insert(self, word):
        current = self

        for letter in word:
            index = Trie.getindex(letter)

            if current.links[index] is None:
                current.links[index] = Trie()

            current = current.links[index]

        current.isword = True

    def iscomplete(self, word):
        current = self
        for letter in word:
            index = Trie.getindex(letter)

            if current.links[index] is None or current.links[index].isword is not True:
                return False
            current = current.links[index]

        return current.isword

    @staticmethod
    def getindex(letter: str):
        return ord(letter) - ord('a')


def completeString(n: int, a: List[str]) -> str:
    t = Trie()
    for word in a:
        t.insert(word)

    cs = ""

    for word in a:
        iscomp = t.iscomplete(word)

        if iscomp:
            if (len(word) > len(cs)) or (len(word) == len(cs) and word < cs):
                cs = word

    return cs if cs != "" else None
