# List

## 2. Add two numbers

题目描述：

![1570451002740](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570451002740.png)

解题思路：

1. 分别定义一个头指针head，和用来做链表移动的指针cur, 让后在定义一个进位标志变量plus。从题意可以看出当前节点的值等于进位变量plus在分别加上两个链表所对应的元素的值，但是需要注意的是两个链表可能长度不一样。还有一个地方需要注意的是，当最后两个链表的值相加刚好有进位的时候，不要忘记把他加在链表的后面,但是这种效率不是很高。



```cpp
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* cur = head;
        int plus = 0;
        while(l1 || l2)
        {
            int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + plus;
            int num = sum % 10;
            plus = sum / 10;
            
            cur->next = new ListNode(num);
            cur = cur->next;
            
            if(l1) l1 = l1->next;
            if(l2) l2 = l2->next;
        }
        if(plus > 0) cur->next = new ListNode(1);
        return head->next;
    }
};
```

![1570451281613](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570451281613.png)



## 206. Reverse Linked List

题目描述：

![1570453411028](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570453411028.png)

解题思路：

1. 最直观的解法就是，定义两个节点pre和next,next用来维护链表的尾部，pre用来维护链表的头部。先让next指向head->next，这样才能保证链表后面的元素可以被访问，然后将head->next指向pre，所以pre应该初始化为NULL，最后再将pre指向head。直到next==NULL结束循环。返回pre.

2. 使用递归的思路来解决这个问题。递归解决这种问题主要分为三步：（1）将head->next之后的所有元素都进行反转（2）反转完之后head->next就变成新链表的最后一个元素，将其余head相连，也就是head->next->next = head（3）最后将head->next指向NULL

```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == NULL || head->next == NULL) return head;
        
        ListNode* pre = NULL;
        ListNode* next = head;
        
        while(next)
        {
            next = head->next;
            head->next = pre;
            pre = head;
            head = next;
        }
        return pre;
    }
};
```

![1570453613629](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570453613629.png)



```cpp
class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == NULL || head->next == NULL) return head;
        ListNode* node = reverseList(head->next);
        head->next->next = head;
        head->next = NULL;
        
        return node;
    }
};
```

![1570454196222](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570454196222.png)

