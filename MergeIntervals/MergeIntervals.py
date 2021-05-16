class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 1:
            return intervals

        pts = [0] * 2 * len(intervals)
        i = 0
        #Create overlap a][a
        for interval in intervals:
            pts[i] = interval[0] * 10
            i += 1
            pts[i] = interval[1] * 10 + 1
            i += 1

        res = []
        pts.sort()
        cnt = 0
        for pt in pts:
            #Start?
            if pt & 1 == 0:
                if cnt == 0:
                    start = pt // 10
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    res.append([start, pt // 10])
        return res



def main():

    s = Solution()

    intervals = [[1,3],[2,6],[8,10],[15,18]]
    res = s.merge(intervals)
    exp = [[1,6],[8,10],[15,18]]
    print("exp = {0} result = {1}".format(exp, res))

    intervals = [[1,4],[4,5]]
    res = s.merge(intervals)
    exp = [[1,5]]
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
    main()