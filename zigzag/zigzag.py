
def convert(s, numRows):

    if numRows == 1:
        return s

    ll = len(s)
    if ll < 3:
        return s

    res = ['\0'] * ll
    ss = ""  
    if numRows == 2:
        # Make it works for odd lines
        p = 0
        for i in range((ll + 1) // 2):
            res[i] = s[p]
            p += 2;

        p = 1;
        for i in range((ll + 1) // 2, ll):
            res[i] = s[p]
            p += 2;
        return ss.join(res);

    cycle = numRows + (numRows - 2)

    tmp = [[] for i in range(numRows)]
    for i in range(ll):
        res1 = i % cycle
        if res1 < numRows:
            tmp[res1].append(s[i])
        else:
            tmp[cycle - res1].append(s[i])

    res = [val for sublist in tmp for val in sublist]

    return ss.join(res);

def main():

    s = "PAYPALISHIRING";
    numRows = 2;
    expect = "PYAIHRNAPLSIIG";
    res = convert(s, numRows);
    print("got %s expects %s cmp %r" % (res, expect, expect == res))

    s = "PAYPALISHIRIN";
    numRows = 2;
    expect = "PYAIHRNAPLSII";
    res = convert(s, numRows);
    print("got %s expects %s cmp %r" % (res, expect, expect == res))

    s = "A";
    numRows = 1;
    expect = "A";
    res = convert(s, numRows);
    print("got %s expects %s cmp %r" % (res, expect, expect == res))

    s = "PAYPALISHIRING";
    numRows = 3;
    expect = "PAHNAPLSIIGYIR";
    res = convert(s, numRows);
    print("got %s expects %s cmp %r" % (res, expect, expect == res))

    s = "PAYPALISHIRING";
    numRows = 4;
    expect = "PINALSIGYAHRPI";
    res = convert(s, numRows);
    print("got %s expects %s cmp %r" % (res, expect, expect == res))

    return 0

if __name__=="__main__":
    main()
