class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ll = len(heights)
        if ll == 0:
            return 0
        if ll == 1:
            return heights[0]
        if ll == 2:
            if heights[0] < heights[1]:
                if 2 * heights[0] > heights[1]:
                    return 2 * heights[0]
                else:
                    return heights[1]
            else:
                if 2 * heights[1] > heights[0]:
                    return 2 * heights[1]
                else:
                    return heights[0]


        heights.append(0)

        wstack = [0]
        hstack = [heights[0]]
        maxs = heights[0]

        for i in range(1, len(heights)):
            lastw = len(heights) + 1
            while len(hstack) > 0 and hstack[-1] > heights[i]:
                lastw = wstack[-1]
                s = (i - lastw) * hstack[-1]
                if s > maxs:
                    maxs = s
                hstack.pop()
                wstack.pop()
            if len(hstack) == 0 or heights[i] > hstack[-1]:
                min = i if i < lastw else lastw
                wstack.append(min)
                hstack.append(heights[i])

        return maxs

def main():
    s = Solution()

    hist = [0, 9]
    exp = 9
    res = s. largestRectangleArea(hist)
    print("exp = {0} result = {1}".format(exp, res))

    hist = [2,2,1,3,4,1,2]
    exp = 7
    res = s. largestRectangleArea(hist)
    print("exp = {0} result = {1}".format(exp, res))

    hist = [2,1,5,6,2,3]
    exp = 10
    res = s. largestRectangleArea(hist)
    print("exp = {0} result = {1}".format(exp, res))

    hist = [2,4]
    exp = 4
    res = s. largestRectangleArea(hist)
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
     main()