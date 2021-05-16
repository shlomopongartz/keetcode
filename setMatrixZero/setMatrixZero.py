class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        zeroStRow = False
        zeroStCol = False
        for x in matrix[0]:
            if x == 0:
                zeroStRow = True
                break
        for x in matrix:
            if x[0] == 0:
                zeroStCol = True
                break
        #Project
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[i])):
                    matrix[i][j] = 0

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(1, len(matrix)):
                    matrix[i][j] = 0

        if zeroStRow:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if zeroStCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        return matrix

def main():

    s = Solution()

    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    res = s.setZeroes(matrix)
    exp = [[1,0,1],[0,0,0],[1,0,1]]
    print("exp = {0} result = {1}".format(exp, res))

    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    res = s.setZeroes(matrix)
    exp = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
    main()