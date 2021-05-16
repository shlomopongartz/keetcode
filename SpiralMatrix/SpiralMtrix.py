class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        oper = ((0,1),(1,0),(0, -1),(-1, 0))
        #One row?
        if len(matrix) == 1:
            return matrix[0]
        #One coloumn?
        if len(matrix[0]) == 1:
            res = [0] * len(matrix)
            for i in range(len(matrix)):
                res[i] = matrix[i][0]
        outsize = len(matrix) * len(matrix[0])
        res = [0] * outsize
        ind = 0
        op = 0
        i = 0
        j = 0
        while (ind < outsize):
            if i < len(matrix) and j < len(matrix[0]) and matrix[i][j] < 1000:
                res[ind] = matrix[i][j]
                ind += 1
                matrix[i][j] += 2000
                i += oper[op][0]
                j += oper[op][1]
            else:
                #revert last oper
                i -= oper[op][0]
                j -= oper[op][1]
                #Try next oper
                op = (op + 1) % 4
                i += oper[op][0]
                j += oper[op][1]

        return res

def main():

    s = Solution()

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    res = s.spiralOrder(matrix)
    exp = [1,2,3,6,9,8,7,4,5]
    print("exp = {0} result = {1}".format(exp, res))

    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    res = s.spiralOrder(matrix)
    exp = [1,2,3,4,8,12,11,10,9,5,6,7]
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
     main()