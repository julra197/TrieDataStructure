#!/usr/bin/env python3
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
#check cat:
print(root.childs[2].childs[0].childs[19].isWord)