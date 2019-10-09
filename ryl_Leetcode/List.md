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

## 83. Remove Duplicates from Sorted List

题目描述：

![1570539016163](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570539016163.png)

解题思路：

1. 这题与数组中删除重复元素的思路很相似，但是需要注意链表的特点。所以可以定义两个指向相邻的节点的指针，当前一个节点的值等于下一个节点的值，那就把后面的那个值删掉，但是对于链表来说需要注意的是，删除元素之前一定要让指针往后移动，不然后面的指针无法访问了，如果两个节点的值不同，那就两个指针同时向后面走一步，知道后一个指针为空

```cpp
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head == NULL || head->next == NULL) return head;
        ListNode* pre = head;
        ListNode* cur = head->next;
        
        while(cur)
        {
            if(pre->val == cur->val) 
            {
                cur = cur->next;
                pre->next = cur;
            }
            else
            {
                pre = pre->next;
                cur = cur->next;
            }
        }
        
        return head;
    }
};
```

## 61. Rotate List

题目描述：

![1570541612679](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570541612679.png)

解题思路：

首先需要看明白题目的意思，题目的意思是将链表旋转k次，只不过这里的旋转的意思指的是将链表的末尾放到链表的头部，算是旋转了一次，所以这里可能出现的情况就是，如果旋转的次数比链表的长度还要长的时候，其实中间就相当于无用功。可以将k对len取模，然后得到最后有效的旋转，然后在将有效旋转的那一部分直接放到链表的头部。如何定位需要整体放到链表头部的那一部分节点可以通过双指针来实现。

先将前面一个指针移动k次，然后再将前后两个指针同时向后移动k步直到最后一个指针指向最后一个元素（也就是first->next==NULL）

```cpp
class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if( !head || !head->next) return head; 
            
        int len = 0;
        for (auto p = head; p; p = p->next) len++;
        k %= len;
        
        auto first = head;
        auto second = head;
        
        while( k-- ) first = first->next;
        
        while(first->next) 
        {
            first = first->next;
            second = second->next;    
        }
        
        first->next = head;
        head = second->next;
        second->next = NULL;
        
        return head;
    }
};
```

## 24. Swap Nodes in Pairs

题目描述：

![1570543965099](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570543965099.png)

解题思路：

这里的主要是对链表中相邻的一个pair进行交换，首先这里会对头结点进行修改，为了减少条件的判断，先增加一个虚拟头结点dummy，然后在每次将两个相邻的pair进行交换。还有一个技巧是正常情况下对于这种pair的操作，可能会想到判断链表的奇偶，然后在进行判断，其实我们可以同时使用一个指针进行判断，也就是p->next && p->next->next这两个都为真的时候才进行处理，也就意味着只有成对的时候才进行处理，否则不进行处理

```cpp
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        auto dummy = new ListNode(-1);
        dummy->next = head;
        
        for(auto p = dummy; p->next && p->next->next; )
        {
            auto a = p->next, b = a->next;
            
            p->next = b;
            a->next = b->next;
            b->next = a;
            p = a;
        }
        
        return dummy->next;
    }
};
```

