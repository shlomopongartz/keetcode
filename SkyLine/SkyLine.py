from operator import itemgetter
import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        lb = len(buildings)
        if lb == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

        events = [None for i in range(lb * 2)]
        j = 0
        for building in buildings:
            events[j] = (building[0], -building[2], building[1])
            j += 1
            events[j] = (building[1], building[2], 1)
            j += 1

        events.sort(key=lambda e: (e[0],e[1]))

        res = []

        top = 0
        heap = []
        heapq.heappush(heap, (0, events[-1][0]))
        for event in events:
            if event[1] < 0:
                #Start
                h = -event[1]
                if h > top:
                    top = h
                    res.append([event[0], h])
                heapq.heappush(heap, (event[1], event[2]))
            else:
                #end
                if event[1] == top:
                    while True:
                        t, end = heapq.heappop(heap)
                        if end <= event[0] and t != 0:
                            continue
                        break
                    heapq.heappush(heap, (t, end))
                    t = -t
                    if t < top:
                        top = t
                        res.append([event[0], top])

        return res

def main():
    s = Solution()

    buildings = [[1,2,1],[1,2,2],[1,2,3]]
    exp = [[1,3],[2,0]]
    res = s.getSkyline(buildings)
    print("exp    = {0}\nresult = {1}".format(exp, res))

    buildings = [[0, 1, 3]]
    exp = [[0,3],[1,0]]
    res = s.getSkyline(buildings)
    print("exp    = {0}\nresult = {1}".format(exp, res))

    buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    exp = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    res = s.getSkyline(buildings)
    print("exp    = {0}\nresult = {1}".format(exp, res))

    buildings = [[0,2,3],[2,5,3]]
    exp = [[0,3],[5,0]]
    res = s.getSkyline(buildings)
    print("exp    = {0}\nresult = {1}".format(exp, res))

if __name__ == "__main__":
    main()
