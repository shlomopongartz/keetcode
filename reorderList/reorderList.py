# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None

        count = 0
        t = head
        while t is not None:
            count += 1
            t = t.next

        if count < 3:
            return head

        #In case of odd first list is longer
        l1 = (count + 1) // 2
        l2 = count - l1
        t = head
        for i in range(l1 - 1):
            t = t.next

        h2 = t.next
        t.next = None

        if h2.next is not None:
            #reverse list 2
            h2 = self.reverse(h2)

        return self.merge(head, h2, l2)

    def reverse(self, head):
        dummy = ListNode(-1, head)
        p = dummy
        c = head
        n = head.next

        while True:
            c.next = p
            p = c
            if n is None:
                break
            c = n
            n = n.next

        #head now points to dummy
        head.next = None
        #This is the new head
        return c

    def merge(self, h1, h2, l2):
        dummy = ListNode(-1, h1)
        head = dummy
        for i in range(l2):
            head.next = h1
            head = head.next
            h1 = h1.next
            head.next = h2
            head = head.next
            h2 = h2.next

        if h1 is not None:
            head.next = h1

        return dummy.next



def mkllist(lst):
    lst.reverse()
    t = ListNode(lst[0])
    for l in lst[1:]:
        t = ListNode(l, t)
    return t

def mklst(head):
    lst = []
    while head is not None:
        lst.append(head.val)
        head = head.next
    return lst

def main():
    sol = Solution()

    lst = [1,2,3,4]
    exp = [1,4,2,3]
    head = mkllist(lst)
    llres = sol.reorderList(head)
    res = mklst(llres)
    print("   exp = {0}\nresult = {1}".format(exp, res))

    lst = [1,2,3,4,5]
    exp = [1,5,2,4,3]
    head = mkllist(lst)
    llres = sol.reorderList(head)
    res = mklst(llres)
    print("   exp = {0}\nresult = {1}".format(exp, res))



if __name__ == "__main__":
    main()