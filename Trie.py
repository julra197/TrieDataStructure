#!/usr/bin/env python3

#Trie data structure for fast storing and retrieving of strings
#Each string in the data structure can be found in constant time

class TrieNode:
    def __init__(self):
        self.isWord = False;
        self.childs = [None] * 27
        
    def populate(self, dictionaryFile):
        for line in dictionaryFile:
            newNode = self
            line = line.lower()
            for char in line:
                slot = ord(char)-97
                if slot != -87:
                    if newNode.childs[slot]==None:
                        newNode.childs[slot] = TrieNode()
                    newNode = newNode.childs[slot]
            newNode.isWord = True
    
    def check(self, word):
        pass




root = TrieNode()
f = open('small', 'r')
root.populate(f)

print(root.childs[3].childs[14].childs[6].childs[6].childs[4].childs)