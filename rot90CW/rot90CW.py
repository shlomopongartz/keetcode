class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ll = len(matrix)
        if ll <= 1:
            return

        for i in range((ll + 1) // 2):
            for j in range(ll // 2):
                ii = i
                jj = j
                t = matrix[ii][jj]
                nii = (ll - 1) - jj
                njj = ii
                matrix[ii][jj] = matrix[nii][njj]
                ii = nii
                jj = njj
                nii = (ll - 1) - jj
                njj = ii
                matrix[ii][jj] = matrix[nii][njj]
                ii = nii
                jj = njj
                nii = (ll - 1) - jj
                njj = ii
                matrix[ii][jj] = matrix[nii][njj]
                ii = nii
                jj = njj
                matrix[ii][jj] = t

def printmatrix(m):
    print('[')
    for line in m:
        print(line)
    print(']')


def compare(m1, m2):
    lm = len(m1)
    for i in range(lm):
        for j in range(lm):
            if m1[i][j] != m2[i][j]:
                print("not match")
                printmatrix(m1)
                printmatrix(m2)
                return
    print("match")

def main():
    s = Solution()

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    exp = [[7,4,1],[8,5,2],[9,6,3]]
    s.rotate(matrix)
    compare(matrix, exp)

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    exp = [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
    s.rotate(matrix)
    compare(matrix, exp)

    matrix = [[1]]
    exp = [[1]]
    s.rotate(matrix)
    compare(matrix, exp)

    matrix = [[1, 2], [3, 4]]
    exp = [[3, 1], [4, 2]]
    s.rotate(matrix)
    compare(matrix, exp)

if __name__ == "__main__":
     main()