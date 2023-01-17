class Trie:
    trie = {}

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        temp = self.trie
        for c in word:
            if not c in temp:
                temp[c] = {}
            temp = temp[c]
        temp[";"] = True
    
    def search(self, word):
        temp = self.trie
        for c in word:
            if not c in temp:
                return False
            temp = temp[c]
        return ";" in temp
    
    def startsWith(self, word):
        temp = self.trie
        for c in word:
            if not c in temp:
                return False
            temp = temp[c]
        return True
            

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)