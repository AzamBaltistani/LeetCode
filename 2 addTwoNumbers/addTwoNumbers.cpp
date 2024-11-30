#include <bits/stdc++.h>
using namespace std;
// Definition for singly-linked list.
struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
{

    // {9, 9, 9, 9, 9, 9, 9, 9}
    // {9, 9, 9, 9, 9}

    ListNode *sumList = new ListNode();
    ListNode *tail = sumList;

    int carry = 0;
    while (true)
    {
        int d1 = (l1 == nullptr) ? 0 : l1->val;
        int d2 = (l2 == nullptr) ? 0 : l2->val;

        int sum = d1 + d2 + carry;

        carry = sum / 10;
        sum = sum % 10;

        tail->val = sum;

        l1 = (l1->next == nullptr) ? nullptr : l1->next;
        l2 = (l2->next == nullptr) ? nullptr : l2->next;
    }
}

void printList(ListNode *list)
{
    ListNode *tail = list;
    while (tail != nullptr)
    {
        cout << tail->val << " ";
        tail = tail->next;
    }
    cout << endl;
}

int main()
{
    // int ll1[] = {1, 6, 0, 3, 3, 6, 7, 2, 0, 1};
    int ll1[] = {9, 9, 9, 9, 9, 9, 9, 9};

    ListNode *l1 = new ListNode();
    ListNode *tail_l1 = l1;

    for (int i = 0; i < sizeof(ll1) / sizeof(ll1[0]) - 1; i++)
    {
        tail_l1->val = ll1[i];
        tail_l1->next = new ListNode(ll1[i + 1]);
        tail_l1 = tail_l1->next;
    }

    // int ll2[] = {6, 3, 0, 8, 9, 6, 6, 9, 6, 1};
    int ll2[] = {9, 9, 9, 9, 9};

    ListNode *l2 = new ListNode();

    ListNode *tail_l2 = l2;
    for (int i = 0; i < sizeof(ll2) / sizeof(ll2[0]) - 1; i++)
    {
        tail_l2->val = ll2[i];
        tail_l2->next = new ListNode(ll2[i + 1]);
        tail_l2 = tail_l2->next;
    }

    printList(l1);
    printList(l2);

    // Expected Output: [7,9,0,1,3,3,4,2,7,2]

    ListNode *ans = addTwoNumbers(l1, l2);

    printList(ans);
}