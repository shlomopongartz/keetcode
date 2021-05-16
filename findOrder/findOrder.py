from collections import deque

class Node(object):
    def __init__(self, i):
        self.i = i
        self.inDegree = 0
        self.nexts = []

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        lp = len(prerequisites)
        if lp == 0:
            return [i for i in range(numCourses)]

        res = []
        #[ai, bi] this means you must take the course bi before the course ai.
        graph = [Node(i) for i in range(numCourses)]
        for prereq in prerequisites:
            graph[prereq[0]].inDegree += 1
            graph[prereq[1]].nexts.append(graph[prereq[0]])

        d = deque(maxlen=numCourses)
        for node in graph:
            if node.inDegree == 0:
                d.append(node)

        count = numCourses
        res = []
        while len(d) > 0:
            node = d.popleft()
            res.append(node.i)
            count -= 1
            for n in node.nexts:
                n.inDegree -= 1
                if n.inDegree == 0:
                    d.append(n)


        if count > 0:
            return []

        return res


def main():
    s = Solution()

    numCourses = 2
    prerequisites = [[1, 0]]
    exp = [0,1]
    res = s.findOrder(numCourses, prerequisites)
    print("exp = {0} result = {1}".format(exp, res))

    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    exp = [0,2,1,3]
    res = s.findOrder(numCourses, prerequisites)
    print("exp = {0} result = {1}".format(exp, res))

    numCourses = 1
    prerequisites = []
    exp = [0]
    res = s.findOrder(numCourses, prerequisites)
    print("exp = {0} result = {1}".format(exp, res))

if __name__ == "__main__":
     main()
