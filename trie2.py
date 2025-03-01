# https://www.naukri.com/code360/problems/implement-trie_1387095
# @AryanERTash

from os import *
from sys import *
from collections import *
from math import *

class Trie:
    def __init__(self):
        self.prefix_count = self.word_count = 0
        self.links = [None] * 26 # none refrence
    
    @staticmethod
    def getindex(ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        current: Trie = self
        
        for letter in word:
            index = Trie.getindex(letter)
            
            if current.links[index] is None:
                current.links[index] = Trie()
            
            
            current = current.links[index]
            current.prefix_count+=1
        
        
        current.word_count += 1

    def countWordsEqualTo(self, word):
        current = self
        
        for letter in word:
            index = Trie.getindex(letter)
            
            if current.links[index] is None:
                return 0
            current = current.links[index]
        
        
        return current.word_count
        

    def countWordsStartingWith(self, word):
        current = self
        
        for letter in word:
            index = Trie.getindex(letter)
            
            if current.links[index] is None:
                return 0
            current = current.links[index]
        
        
        return current.prefix_count

    def erase(self, word):
        # assuming word exists in the Trie
        current = self
        
        for letter in word:
            index = Trie.getindex(letter)
            current.links[index].prefix_count-=1
            next = current.links[index]
            
            if current.links[index].prefix_count == 0:
                current.links[index] = None
            
            
            current = next
        
        
        current.word_count-=1
        
            
            
            
