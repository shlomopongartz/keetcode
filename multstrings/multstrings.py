class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        a = self.strToList(num1)
        b = self.strToList(num2)

        t = self.Karatsuba(a, b)

        return self.listToStr(t)

    def add(self, num1, num2):
        a = self.strToList(num1)
        b = self.strToList(num2)

        t = self.aPLUSb(a, b)

        return self.listToStr(t)

    def minus(self, num1, num2):
        a = self.strToList(num1)
        b = self.strToList(num2)

        t = self.aMINUSb(a, b)

        return self.listToStr(t)

    def strToList(self, num):
        la = len(num)
        a = [0] * la
        i = la
        for c in num:
            i -= 1
            a[i] = ord(c) - ord('0')
        return a

    def listToStr(self, t):
        r = [''] * len(t)
        j = len(t) - 1
        for i in range(len(t)):
            r[j] = chr(t[i] + ord('0'))
            j -= 1
        s = ''
        return s.join(r)

    def aPLUSb(self, a, b):
        la = len(a)
        if la == 0:
            return b

        lb = len(b)
        if lb == 0:
            return a

        if la < lb:
            lmin = la
            lmax = lb
            m = b
        else:
            lmin = lb
            lmax = la
            m = a

        res = [0] * (lmax + 1)
        c = 0
        for i in range(lmin):
            s = a[i] + b[i] + c
            if s > 9:
                c = 1
                s -= 10
            else:
                c = 0
            res[i] = s

        for i in range(lmin, lmax):
            s = m[i] + c
            if s > 9:
                c = 1
                s -= 10
            else:
                c = 0
            res[i] = s

        if c > 0:
            res[lmax] = 1
            return res
        else:
            return res[:lmax]

    def aMINUSb(self, a, b):
        lb = len(b)
        if lb < 2:
            if lb == 0:
                return a
            if lb == 1 and b[0] == 0:
                return a
        if lb < len(a):
            ll = len(a)
        else:
            ll = lb
        TensComp = [0] * ll
        firstNonZero = ll
        for ind, x in enumerate(b):
            if x != 0:
                firstNonZero = ind
                break
        if firstNonZero < ll:
            TensComp[firstNonZero] = 10 - b[firstNonZero]
        for i in range(firstNonZero + 1, lb):
            TensComp[i] = 9 - b[i]
        for i in range(lb, ll):
            TensComp[i] = 9
        diff = self.aPLUSb(a, TensComp)
        #remove the overflow
        diff[-1] = 0
        #Chop leading zeros
        for ind in range(len(diff) - 1, -1, -1):
            if diff[ind] != 0:
                break
        ind += 1
        return diff[0:ind]

    def smallMult(self, a, b):
        if len(a) == 1 and len(b) == 1:
            z = a[0] * b[0]
            if z > 9:
                return [z%10, z//10]
            else:
                return [z]
        aR = a[0]
        aL = 0 if len(a) == 1 else a[1]
        bR = b[0]
        bL = 0 if len(b) == 1 else b[1]
        z = ((aL * 10) + aR) * ((bL * 10) + bR)

        res = [0] * 4
        res[3] = z // 1000
        z = z % 1000
        res[2] = z // 100
        z = z % 100
        res[1] = z // 10
        z = z % 10
        res[0] = z

        if res[3] > 0:
            return res[0:4]
        if res[2] > 0:
            return res[0:3]
        if res[1] > 0:
            return res[0:2]
        return res[0:1]

    def specialCases(self, a, b):
        if len(a) == 1:
            if a[0] == 0:
                return [0]
            elif a[0] == 1:
                return b
            elif a[0] == 2:
                return self.aPLUSb(b, b)
        if len(b) == 1:
            if b[0] == 0:
                return [0]
            elif b[0] == 1:
                return a
            elif b[0] == 2:
                return self.aPLUSb(a, a)
        return None

    def Karatsuba(self, a,b):
        #Algorithm Karatsuba(a,b):
        #if a or b has one digit, then:
        #    return a * b.
        #else:
        #    Let n be the number of digits in max{a, b}.
        #    Let aL and aR be left and right halves of a.
        #    Let bL and bR be left and right halves of b.
        #    Let x1 hold Karatsuba(aL, bL).
        #    Let x2 hold Karatsuba(aL + aR, bL + bR).
        #    Let x3 hold Karatsuba(aR, bR).
        #    return x1*10n + (x2 - x1 - x3)*10n/2 + x3.
        #end of if
        if len(a) < 3 or len(b) < 3:
            if len(a) == 0 or len(b) == 0:
                return [0]
            res = self.specialCases(a, b)
            if res is not None:
                return res
            if len(a) < 3 and len(b) < 3:
                return self.smallMult(a, b)

        la = len(a)
        lb = len(b)
        lmax = la if la > lb else lb
        n = (lmax + 1) // 2
        x1 = self.Karatsuba(a[n:], b[n:])
        AlPlusAr = self.aPLUSb(a[n:],a[:n])
        BlPlusBr = self.aPLUSb(b[n:],b[:n])
        x2 = self.Karatsuba(AlPlusAr, BlPlusBr)
        x3 = self.Karatsuba(a[:n], b[:n])
        if x1 == [0]:
            t1 = x1
        else:
            t1 = [0] * (n + n)
            t1 += x1
        t2 = self.aPLUSb(x1, x3)
        m = self.aMINUSb(x2, t2)
        if m == [0]:
            t3 = m
        else:
            t3 = [0] * n
            t3 += m
        t4 = self.aPLUSb(t1, t3)
        t5 = self.aPLUSb(t4, x3)

        return t5


def main():
    s = Solution()

    num1 = "9123"
    num2 = "8456"
    res = s.add(num1, num2)
    exp = "17579"
#    print("exp = {0} result = {1}".format(exp, res))

    num1 = "9123"
    num2 = "8456"
    res = s.minus(num1, num2)
    exp = "667"
#    print("exp = {0} result = {1}".format(exp, res))

    num1 = "408"
    num2 = "5"
    res = s.multiply(num1, num2)
    exp = "2040"
    print("exp = {0} result = {1}".format(exp, res))

    num1 = "23650399"
    num2 = "1148"
    res = s.multiply(num1, num2)
    exp = "27150658052"
    print("exp = {0} result = {1}".format(exp, res))

    num1 = "9133"
    num2 = "0"
    res = s.multiply(num1, num2)
    exp = "0"
    print("exp = {0} result = {1}".format(exp, res))

    num1 = "999"
    num2 = "999"
    res = s.multiply(num1, num2)
    exp = "998001"
    print("exp = {0} result = {1}".format(exp, res))


    num1 = "2"
    num2 = "3"
    res = s.multiply(num1, num2)
    exp = "6"
    print("exp = {0} result = {1}".format(exp, res))

    num1 = "20"
    num2 = "3"
    res = s.multiply(num1, num2)
    exp = "60"
    print("exp = {0} result = {1}".format(exp, res))

    num1 = "2"
    num2 = "30"
    res = s.multiply(num1, num2)
    exp = "60"
    print("exp = {0} result = {1}".format(exp, res))

    num1 = "20"
    num2 = "30"
    res = s.multiply(num1, num2)
    exp = "600"
    print("exp = {0} result = {1}".format(exp, res))

    num1 = "11"
    num2 = "11"
    res = s.multiply(num1, num2)
    exp = "121"
    print("exp = {0} result = {1}".format(exp, res))

    num1 = "123"
    num2 = "456"
    res = s.multiply(num1, num2)
    exp = "56088"
    print("exp = {0} result = {1}".format(exp, res))

    num1 = "1024"
    num2 = "1024"
    res = s.multiply(num1, num2)
    exp = "1048576"
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
     main()