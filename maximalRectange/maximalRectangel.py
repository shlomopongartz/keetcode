class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0

        if len(matrix[0]) == 0:
            return 0

        max = -1
        hist = [0] * len(matrix[0])
        for row in matrix:
            for col, x in enumerate(row):
                if x == '0':
                    hist[col] = 0
                else:
                    hist[col] += 1
            val = self.largestRectangleArea(hist)
            if val > max:
                max = val
        return max

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

        #Remove added sentinel
        heights.pop()
        return maxs

    def maximalRectangle2(self, matrix):
        rows = len(matrix)
        if rows == 0:
            return 0

        cols = len(matrix[0])
        if rows == 0:
            return 0

        dph = [[0 for col in range(cols)] for row in range(2)]
        dpl = [[0 for col in range(cols)] for row in range(2)]
        dpr = [[(cols - 1) for col in range(cols)] for row in range(2)]

        maxs = 0

        rr = 0
        pr = 1
        for row in matrix:
            rr = 1 - rr
            pr = 1 - pr
            for c, x in enumerate(row):
                if x == "1":
                    dph[rr][c] = dph[pr][c] + 1
                else:
                    dph[rr][c] = 0

            lb = 0
            for c, x in enumerate(row):
                if x == "0":
                    lb = c + 1
                    dpl[rr][c] = 0
                else:
                    dpl[rr][c] = max(lb, dpl[pr][c])


            rb = cols
            for c in range(cols - 1, -1, -1):
                x = row[c]
                if x == "0":
                    rb = c - 1
                    dpr[rr][c] = cols - 1
                else:
                    dpr[rr][c] = min(rb, dpr[pr][c])

            for i in range(cols):
                diff = dpr[rr][i] - dpl[rr][i] + 1
                s = diff * dph[rr][i]
                if s > maxs:
                    maxs = s

        return maxs


def main():
    s = Solution()

    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    exp = 6
    res = s.maximalRectangle(matrix)
    print("exp = {0} result = {1}".format(exp, res))
    res = s.maximalRectangle2(matrix)
    print("exp = {0} result = {1}".format(exp, res))

    matrix = []
    exp = 0
    res = s.maximalRectangle(matrix)
    print("exp = {0} result = {1}".format(exp, res))
    res = s.maximalRectangle2(matrix)
    print("exp = {0} result = {1}".format(exp, res))


if __name__ == "__main__":
     main()