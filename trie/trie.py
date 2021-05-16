class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.term = False
        self.childrens = [None for i in range(ord('z') - ord('a') + 1)]

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        if word == "":
            self.term = True
            return
        o = ord(word[0]) - ord('a')
        if self.childrens[o] is None:
            self.childrens[o] = Trie()
        self.childrens[o].insert(word[1:])

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if word == "":
            if self.term:
                return True
            else:
                return False
        o = ord(word[0]) - ord('a')
        if self.childrens[o] is None:
            return False
        else:
            return self.childrens[o].search(word[1:])


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if prefix == "":
            return True
        o = ord(prefix[0]) - ord('a')
        if self.childrens[o] is None:
            return False
        else:
            return self.childrens[o].startsWith(prefix[1:])

def main():
    trie = Trie()

    trie.insert("apple")

    exp = True
    res = trie.search("apple")
    print("exp = {0} result = {1}".format(exp, res))

    exp = False
    res = trie.search("app")
    print("exp = {0} result = {1}".format(exp, res))

    exp = True
    res = trie.startsWith("app")
    print("exp = {0} result = {1}".format(exp, res))

    trie.insert("app")
    exp = True
    res = trie.search("app")
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
     main()
