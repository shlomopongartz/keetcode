
def longestValidParentheses(s):
    ll = len(s)
    stack = [None] * (ll + 2)
    
    stack[0] = (')', -1)
    sp = 1
    for i, x in enumerate(s):
        if x == '(':
            stack[sp] = ('(', i)
            sp += 1
        elif stack[sp - 1][0] == '(':
            sp -= 1
        else:
            stack[sp] = (')', i)
            sp += 1

    stack[sp] = ('(', ll)
    sp += 1

    maxgap = -1
    for i in range(1, sp):
        gap = stack[i][1] - stack[i - 1][1]
        if gap > maxgap:
            maxgap = gap

    return maxgap - 1

def main():
    s = "(()"
    print("s is %s p is %d" % (s, longestValidParentheses(s)))
    s = ")()())"
    print("s is %s p is %d" % (s, longestValidParentheses(s)))
    s = ""
    print("s is %s p is %d" % (s, longestValidParentheses(s)))

if __name__=="__main__":
    main()
