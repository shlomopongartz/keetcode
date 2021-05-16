class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        ll = len(matrix)
        if ll <= 1:
            return
        #Transpos
        for i in range(ll - 1):
            for j in range(i + 1, ll):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #Mirror
        for i in range(ll):
            for j in range((ll + 1) // 2):
                matrix[i][j],  matrix[i][ll - j - 1] =  matrix[i][ll - j - 1],  matrix[i][j]


def compare(m1, m2):
    lm = len(m1)
    for i in range(lm):
        for j in range(lm):
            if m1[i][j] != m2[i][j]:
                print("not match")
                return
    print("match")

def main():
    s = Solution()

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