#include <stdio.h>

struct ListNode {
     int val;
     struct ListNode *next;
};


struct ListNode* removeNthFromEnd(struct ListNode* head, int n)
{
    struct ListNode dummy;
    struct ListNode *p;

    dummy.next = head;
    p = &dummy;
    for (--n; n ; --n) {
        /* 1 <= sz and n <= sz so no need to check */
        p = p->next;
    }
    /* p points to one node before the Nth element */
    p->next = p->next->next;
    return dummy.next;
}


void test1()
{
	struct ListNode a[5] = {{1,&a[1]},{2,&a[2]},{3,&a[3]},{4,&a[4]},{5,NULL}};
	struct ListNode *newhead = removeNthFromEnd(a, 2);
}

void test2()
{
	struct ListNode a[1] = {{5,NULL}};
	struct ListNode *newhead = removeNthFromEnd(a, 1);
}

int main()
{
	test1();
	//test2();
	return 0;
}
