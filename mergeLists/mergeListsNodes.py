import heapq

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    ll = len(lists)
    if ll == 0:
        return None
    if ll == 1:
        return lists[0]

    ptrs = lists[:]
    heap = [] * ll
    for ind, l in enumerate(ptrs):
        if l is not None:
            heapq.heappush(heap, l.val * 100000 + ind)
            ptrs[ind] = l.next
        else:
            ll -= 1

    head = ListNode(-1)
    out = head

    while (ll):
        x = heapq.heappop(heap)
        val = x // 100000
        ind = x % 100000
        out.next = lists[ind]
        out = out.next
        lists[ind] = lists[ind].next
        if ptrs[ind] is not None:
            heapq.heappush(heap, ptrs[ind].val * 100000 + ind)
            ptrs[ind] = ptrs[ind].next
        else:
            ll -= 1

    return head.next

def printList(n):
    while n is not None:
        print("%d ->", n.val)
        n = n.next

def main():
    n10 = ListNode(5)
    n11 = ListNode(4,n10)
    n12 = ListNode(1,n11)
    n20 = ListNode(4)
    n21 = ListNode(3, n20)
    n22 = ListNode(1, n21)
    n30 = ListNode(6)
    n31 = ListNode(2, n30)
    s = [n12, n22, n31]
    n = mergeKLists(s)
    print("s is %s p is %r" % (s, printList(n)))
    s = [None]
    n = mergeKLists(s)
    print("s is %s p is %r" % (s, printList(n)))
    s = []
    n = mergeKLists(s)
    print("s is %s p is %r" % (s, printList(n)))

if __name__=="__main__":
    main()
