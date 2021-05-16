class Shift:
    def __init__(self, len, mod):
        self.tbl = [0] * (ord('z') - ord('a') + 1)
        for i in range(1, ord('z') - ord('a') + 1):
            h = i
            for l in range(len-1):
                h = (h << 5) % mod
            self.tbl[i] = h;

    def shifted(self, n):
        return self.tbl[n]


def hashfunc(s, mod):
    h = 0
    for l in s:
        h = ((h << 5) + ord(l) - ord('a')) % mod
    return h

def hashfuncN(s, i, n, mod):
    h = 0
    for j in range(i, n):
        h = ((h << 5) + ord(s[j]) - ord('a')) % mod
    return h

def rehashfunc(s, runhash, ind, lword, mod, shift):
    runhash = runhash + mod - shift.shifted(ord(s[ind]) - ord('a'))
    runhash = (runhash << 5) % mod
    runhash = (runhash + ord(s[ind + lword]) - ord('a')) % mod
    return runhash


def findSubstring(s, words):
    ls = len(s)
    lwords = len(words)
    if lwords == 0:
        return []
    lword = len(words[0])
    if lwords * lword > ls:
        return []

    bits = lwords.bit_length()
    if lwords & (lwords - 1) != 0:
        bits += 1
    #Double the size
    hash_size = 2 << bits
    mod = hash_size - 1

    shift = Shift(lword, mod)

    wordrep = [0] * (lwords + 1)
    weights = [0] * (lwords + 1)
    wordshash = [None] * hash_size
    i = 1
    weight = 1
    for word in words:
        hashval = hashfunc(word, mod);
        entry = wordshash[hashval]
        if entry == None:
            wordshash[hashval] = [(word, i)]
            wordrep[i] = 1
            weights[i] = weight
            i += 1
            weight = (weight * lwords) % 8191
        else:
            isNew = True
            for w, j in entry:
                if w == word:
                    wordrep[j] += 1
                    isNew = False
                    break
            if isNew:
                entry.append((word, i))
                wordrep[i] = 1
                weights[i] = weight
                i += 1
                weight = (weight * lwords) % 8191

    target = 0
    for i, a in enumerate(wordrep):
        target = (target + weights[i] * a) % 8191

    res = []
    window = lwords * lword
    matches = [0] * window
    matchesN = [0] * window
    x = 0

    runhash = hashfuncN(s, 0, lword, mod)
    currsum = [0] * lword
    currN = [0] * lword
    y = 0;
    #For last hash (last hash will not be used
    s = s + 'x'
    for i in range(ls - lword + 1):
        entry = wordshash[runhash]
        currsum[y] = (currsum[y] + 8191 - matches[x]) % 8191
        currN[y] -= matchesN[x]
        matches[x] = 0
        matchesN[x] = 0
        if entry is not None:
            # We may have collisions
            for opt in entry:
                if opt[0] == s[i:i+lword]:
                    matches[x] = weights[opt[1]]
                    currsum[y] = (currsum[y] + matches[x]) % 8191
                    matchesN[x] = 1
                    currN[y] += 1
                    #The example hase the word "word" twice!
                    if currsum[y] == target and currN[y] == lwords:
                        res.append(i - (lwords - 1) * lword)
        x = (x + 1) % window
        y = (y + 1) % lword
        runhash = rehashfunc(s, runhash, i, lword, mod, shift)
    return res

def main():
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    result = findSubstring(s, words)
    print(result)
    print([])

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "good"]
    result = findSubstring(s, words)
    print(result)
    print([8])

    s = "barfoothefoobarman"
    words = ["foo","bar"]
    result = findSubstring(s, words)
    print(result)
    print([0,9])

    s = "aaaaaaaaaaaaaa"
    words = ["aa", "aa"]
    result = findSubstring(s, words)
    print(result)
    print([0,1,2,3,4,5,6,7,8,9,10])

    s = "barfoofoobarthefoobarman"
    words = ["bar","foo","the"]
    result = findSubstring(s, words)
    print(result)
    print([6,9,12])

if __name__=="__main__":
    main()
