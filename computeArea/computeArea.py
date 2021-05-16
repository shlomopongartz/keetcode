class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        minx = A if A > E else E
        miny = B if B > F else F
        maxx = C if C < G else G
        maxy = D if D < H else H

        dx = maxx - minx
        dy = maxy - miny
        if dx <= 0:
            common = 0
        elif dy <= 0:
            common = 0
        else:
            common = dx * dy

        return (C - A) * (D - B) + (G - E) * (H - F) - common


def main():
    s = Solution()

    A = -3
    B = 0
    C = 3
    D = 4
    E = 0
    F = -1
    G = 9
    H = 2
    exp = 45
    res = s.computeArea(A, B, C, D, E, F, G, H)

    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
     main()
