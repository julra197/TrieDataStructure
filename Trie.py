#!/usr/bin/env python3

#Trie data structure for fast storing and retrieving of strings
#Each string in the data structure can be found in constant time


class TrieNode:
    def __init__(self):
        self.isWord = False;
        self.childs = [None] * 27
        self.counter = 0
        
    def populate(self, dictionaryFile):
        #process each line, where each line is a unique string for the dictionary
        for line in dictionaryFile:
            newNode = self
            #all lowercase
            line = line.lower()
            #populate the trie:
            for char in line:
                slot = ord(char)-97
                if slot >= 0 and slot <=26:
                    if newNode.childs[slot]==None:
                        newNode.childs[slot] = TrieNode()
                    newNode = newNode.childs[slot]
            #after last character set is word to true
            newNode.isWord = True
            #check wheter all words are stored:
            self.counter +=1
    
    def check(self, word):
        currentLevel = self
        word = word.lower()
        for char in word:
            slot = ord(char)-97
            if(currentLevel.childs[slot] != None):
                currentLevel = currentLevel.childs[slot]
            else:
                return False
        return currentLevel.isWord
    
    #len and count do not properly work
    def count(self, node):
        if node.isWord:
            self.counter += 1
        for i in range(27):
            if(node.childs[i] != None):
                self.count(node.childs[i])
        return self.counter
    
    def __len__(self):
        self.counter = 0
        count = self.count(self)
        self.counter = None
        return count
   
    



dictionary = TrieNode()
d = open('large', 'r')
dictionary.populate(d)
print(dictionary.check("a"))
print(dictionary.check("hencoop"))
print(dictionary.check("zymurgy"))
print(dictionary.counter)
print(len(dictionary))