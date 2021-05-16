class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        byI = [0] * 9
        byJ = [0] * 9
        byQ = [0] * 9

        for i, line in enumerate(board):
            t = (i // 3) * 3
            for j, x in enumerate(line):
                if x == '.':
                    continue
                val = ord(x) - ord('0')
                bit = 1 << val
                if byI[i] & bit:
                    return False
                if byJ[j] & bit:
                    return False
                q = t + j // 3
                if byQ[q] & bit:
                    return False
                byI[i] |= bit
                byJ[j] |= bit
                byQ[q] |= bit

        return True

def main():
    s = Solution()

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    exp = True
    print("exp = {0} result = {1}".format(exp, s.isValidSudoku(board)))

    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    exp = False
    print("exp = {0} result = {1}".format(exp, s.isValidSudoku(board)))

