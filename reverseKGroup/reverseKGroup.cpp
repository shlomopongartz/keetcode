#include <iostream>
#include <memory>


struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
private:
	int reverseGroup(ListNode *prehead, int k, ListNode **nn)
	{
		ListNode *p;
		ListNode *q;
		ListNode *b4;
		ListNode *end;
		ListNode *n;

		q = prehead;
		p = prehead->next; // the head what need to be reversed
		if (!p) {
			return k;
		}
		b4 = q;
		end = p;
		for (; k && p != nullptr; --k) {
			n = p->next;
			p->next = q;
			q = p;
			p = n;
		}
		b4->next = q;
		end->next = p;
		*nn = end;
		return k;
	}
public:
	ListNode* reverseKGroup(ListNode* head, int k)
	{
		if (k <= 1 || head == nullptr)
			return head;

		ListNode prehead(0, head);
		ListNode *p = &prehead;
		ListNode *n;

		int kk = k;
		while ((kk = reverseGroup(p, k, &n)) == 0) {
			p = n;
			kk = k;
		}
		if (kk != 0) {
			// Reverse back last segment
			reverseGroup(p, k - kk, &n);
		}
		return prehead.next;
	}
};


// These are the tests we use to determine if the solution is correct.
// You can add your own at the bottom, but they are otherwise not editable!
void printLinkedList(ListNode *head)
{
	std::cout << "[";
	while (head != NULL) {
		std::cout << head->val;
		head = head->next;
		if (head != NULL)
			std::cout << " ";
	}
	std::cout << "]\n";
}

ListNode* createLinkedList(int arr[], int size)
{
	ListNode dummy;
	ListNode *t = &dummy;

	for (int i = 0; i < size; ++i)
	{
		ListNode *n = new ListNode(arr[i]);
		t->next = n;
		t = n;
	}
	return dummy.next;
}

void compareLists(ListNode *p, ListNode *q)
{
	while (p != nullptr && q != nullptr) {
		if (p->val != q->val) {
			std::cout << "Lists mismatch" << std::endl;
			return;
		}
		p = p->next;
		q = q->next;
	}
	if (p != nullptr || q != nullptr) {
		std::cout << "Lists mismatch" << std::endl;
		return;
	}
	std::cout << "Lists match" << std::endl;
	return;
}

int main()
{
	Solution s;
	{
		int arr[] = {1,2,3,4,5};
		int expected[] = {2,1,4,3,5};
		int size = sizeof(arr)/sizeof(arr[0]);
		ListNode *head = createLinkedList(arr, size);
		ListNode *exp = createLinkedList(expected, size);
		printLinkedList(head);
		printLinkedList(exp);
		ListNode *result = s.reverseKGroup(head, 2);
		printLinkedList(result);
		compareLists(result, exp);
	}
	{
		int arr[] = {1,2,3,4,5};
		int expected[] = {3,2,1,4,5};
		int size = sizeof(arr)/sizeof(arr[0]);
		ListNode *head = createLinkedList(arr, size);
		ListNode *exp = createLinkedList(expected, size);
		printLinkedList(head);
		printLinkedList(exp);
		ListNode *result = s.reverseKGroup(head, 3);
		printLinkedList(result);
		compareLists(result, exp);
	}
	{
		int arr[] = {1,2,3,4,5};
		int expected[] = {1,2,3,4,5};
		int size = sizeof(arr)/sizeof(arr[0]);
		ListNode *head = createLinkedList(arr, size);
		ListNode *exp = createLinkedList(expected, size);
		ListNode *result = s.reverseKGroup(head, 1);
		printLinkedList(result);
		compareLists(result, exp);
	}
	{
		int arr[] = {1};
		int expected[] = {1};
		int size = sizeof(arr)/sizeof(arr[0]);
		ListNode *head = createLinkedList(arr, size);
		ListNode *exp = createLinkedList(expected, size);
		ListNode *result = s.reverseKGroup(head, 1);
		compareLists(result, exp);
	}
}
