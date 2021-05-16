
def longestPalindrome(s):
    ll = len(s)
    sll = 2 * ll + 1
    arr = ['#'] * (sll + 2)
    for i in range(ll):
        arr[2 * i + 1] = s[i]
    #To break the inner loop only by comparison
    arr[sll] = '$'
    # -1 index
    arr[sll + 1] = '@'

    extend = [0] * (sll + 2)
    r = 0
    #Current
    c = 0
    i = 1
    while r < sll - 1:
        if i > r:
            r = i
        else:
            mirr_i = c - (i - c)
            if i + extend[mirr_i] < r:
                extend[i] = extend[mirr_i]
                i += 1
                continue

            extend[i] = r - i

        # Try to push the bounderies
        r = i + extend[i] + 1
        l = i - extend[i] - 1
        while arr[l] == arr[r]:
            r += 1
            l -= 1
            extend[i] += 1

        #We have on extra
        r -= 1
        l += 1

        if i + extend[i] >= c + extend[c]:
            c = i

        i += 1


    m = extend[0]
    ind = 0
    #Don't care about the last #
    for i in range(sll):
        if extend[i] > m:
            m = extend[i]
            ind = i

    #In both odd and even case first letter is always '#'
    r = (ind + extend[ind]) // 2
    l = (ind - extend[ind]) // 2

    out = s[l:r]

    return out

def main():
    s = "babad"
    print("s is %s p is %s" % (s, longestPalindrome(s)))
    s = "sbbd"
    print("s is %s p is %s" % (s, longestPalindrome(s)))
    s = "a"
    print("s is %s p is %s" % (s, longestPalindrome(s)))
    s = "ac"
    print("s is %s p is %s" % (s, longestPalindrome(s)))

if __name__=="__main__":
    main()
