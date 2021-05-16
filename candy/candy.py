class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        lr = len(ratings)
        ltr = [1] * lr
        rtl = [1] * lr

        j = lr - 2
        for i in range(1, lr):
            if ratings[i] > ratings[i-1]:
                ltr[i] = ltr[i-1] + 1
            if ratings[j] > ratings[j+1]:
                rtl[j] = rtl[j+1] + 1
            j -= 1

        max = 0
        for i in range(lr):
            if ltr[i] > rtl[i]:
                max += ltr[i]
            else:
                max += rtl[i]

        return max


def main():
    s = Solution()

    ratings = [1, 2, 87, 87, 87, 2, 1]
    exp = 13
    res = s.candy(ratings)
    print("exp = {0} result = {1}".format(exp, res))

    ratings = [1,0,2]
    exp = 5
    res = s.candy(ratings)
    print("exp = {0} result = {1}".format(exp, res))

    ratings = [1,2,2]
    exp = 4
    res = s.candy(ratings)
    print("exp = {0} result = {1}".format(exp, res))


if __name__ == "__main__":
    main()
