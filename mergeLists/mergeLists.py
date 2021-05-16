import heapq

def mergeKLists(lists):
    ll = len(lists)
    if ll == 0:
        return []
    if ll == 1:
        return lists[0]

    heap = [] * ll
    db = [None] * ll
    total = 0
    for ind, l in enumerate(lists):
        db[ind] = [len(l), 0]
        total += db[ind][0]
        if db[ind][0] > 0:
            heapq.heappush(heap, l[0] * 100000 + ind)
            db[ind][0] -= 1
            db[ind][1] = 1

    out = [0] * total
    for i in range(total):
        x = heapq.heappop(heap)
        val = x // 100000
        ind = x % 100000
        if db[ind][0] > 0:
            heapq.heappush(heap, lists[ind][db[ind][1]] * 100000 + ind)
            db[ind][0] -= 1
            db[ind][1] += 1
        out[i] = val

    return out

def main():
    s = [[1,4,5],[1,3,4],[2,6]]
    print("s is %s p is %r" % (s, mergeKLists(s)))
    s = []
    print("s is %s p is %r" % (s, mergeKLists(s)))
    s = [[]]
    print("s is %s p is %r" % (s, mergeKLists(s)))

if __name__=="__main__":
    main()
