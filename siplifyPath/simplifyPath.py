class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        lst = path.split('/')
        for l in lst:
            if len(l) == 0:
                continue
            if l == '.':
                continue
            if l == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(l)
        str = '/'
        return str + str.join(stack)

def main():
    s = Solution()

    path = "/home/"
    exp = "/home"
    res = s.simplifyPath(path)
    print("exp = {0} result = {1}".format(exp, res))

    path = "/../"
    exp = "/"
    res = s.simplifyPath(path)
    print("exp = {0} result = {1}".format(exp, res))

    path = "/home//foo/"
    exp = "/home/foo"
    res = s.simplifyPath(path)
    print("exp = {0} result = {1}".format(exp, res))

    path = "/a/./b/../../c/"
    exp = "/c"
    res = s.simplifyPath(path)
    print("exp = {0} result = {1}".format(exp, res))



if __name__ == "__main__":
    main()
