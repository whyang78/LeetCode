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



## 92. Reverse Linked List II

题目描述：

![1570631927562](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570631927562.png)

解题思路：

![1570631970675](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570631970675.png)

```cpp
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if( !head || !head->next || m == n) return head;
        
        auto dummy = new ListNode(-1);
        dummy->next = head;
        
        auto a = dummy, d = dummy;
        for (int i = 0; i < m - 1; i++) a = a->next;
        for (int i = 0; i < n; i++) d = d->next;
        
        auto b = a->next, c = d->next; 
        for (auto p = b, q = b->next; q != c;)
        {
            auto o = q->next;
            q->next = p;
            p = q, q = o;
        }
        
        a->next = d;
        b->next = c;
        
        return dummy->next;
    }
};
```

代码优化：只遍历一次O(n)

```cpp
class Solution {
public:
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if( !head || !head->next || m == n) return head;
        
        auto dummy = new ListNode(-1);
        dummy->next = head;
        
        auto p = dummy;
        for (int i = 0; i < m -1; i++) p = p->next;
        
        auto a = p, b = a->next, c = b->next;
        for (int i = m + 1; i <= n; i++)
        {
            auto d = c->next;
            c->next = b;
            b = c, c = d;
        }
        
        a->next->next = c;
        a->next = b;
        
        return dummy->next;
    }
};
```



## 160. Intersection of two Linked List

题目描述：

![1570633586948](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570633586948.png)

![1570633601779](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570633601779.png)

解题思路：

![1570633657089](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570633657089.png)

```cpp
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        auto p = headA, q = headB;
        
        while( p != q )
        {
            if ( p ) p = p->next;
            else p = headB;
            
            if ( q ) q = q->next;
            else q = headA;
        }            
        
        return p;
    }
};
```



## 86. Partition List

题目描述：

![1570715364532](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570715364532.png)

解题思路：

使用两个链表分别记录比输入的x小的元素以及大于等于x的元素。最后将较小的那个链表接在较大值链表的后面

```cpp
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* left = new ListNode(-1);
        ListNode* right = new ListNode(-1);
        
        ListNode *pl = left, *pr = right;
        for (ListNode *p = head; p; p = p->next)
            if (p->val < x)
            {
                pl->next = p;
                pl = pl->next;
            }
            else
            {
                pr->next = p;
                pr = pr->next;
            }
        
        pl->next = right->next;
        pr->next = NULL;
        
        return left->next;
    }
};
```

## 141. Linked List Cycle

题目描述：

![1570795330788](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570795330788.png)

解题思路：

使用快慢指针，快指针每次走两步，满指针每次走一步，如果快慢指针能够相遇，则说明链表有环

```cpp
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if ( !head || !head->next ) return false;
        
        auto fast = head, slow = head;
        
        while( fast && fast->next )
        {
            slow = slow->next;
            fast = fast->next->next;
            
            if ( fast == slow ) return true;
        }
        
        return false;
    }
};

```

## 142. Linked List Cycle II

题目描述：

![1570715872022](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570715872022.png)

解题思路：

![1570717818692](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570717818692.png)

这道题有一种非常巧妙的做法，也是使用快慢指针，首先让快指针与慢指针同时往后分别走两步和一步，当

快慢指针相遇之后，让满指针回到起点，快慢指针同时一起每次往后移动一步，直到快慢指针相遇的时候，相遇点就是环的入口

```cpp
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        auto fast = head, slow = head;
        
        while(fast && slow)
        {
            fast = fast->next;
            slow = slow->next;
            if (fast) fast = fast->next;
            else break;
            
            if (fast == slow)
            {
                slow = head;
                
                while (fast != slow)
                {
                    fast = fast->next;
                    slow = slow->next;
                }
                
                if (fast == slow) return fast;
            }
        }
        
        return NULL;
    }
};
```

## 82. Remove Duplicates from Sorted List II 

题目描述：

![1570720586336](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570720586336.png)

解题思路：

```cpp
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head || !head->next) return head;
        
        auto dummy = new ListNode(-1);
        dummy->next = head;

        auto p = dummy, q = head;
        
        while ( q )
        {
            while ( q->next && q->val == q->next->val) q = q->next;
            if ( p->next == q) p = q;
            else p->next = q->next;
            
            q = q->next;
        }
        
        return dummy->next;
    }
};
```

## 19. Remove Nth Node From End of List

题目描述：

![1570795495462](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570795495462.png)

解题思路：

使用快慢指针，先让快指针走N步，然后慢指针（在dummy处）与快指针同时往后走一步，直到快指针的next为空，则慢指针所对应的就是倒数第N个节点的上一个节点，因为快慢指针之间相差N个节点

```cpp
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        auto dummy = new ListNode(-1);
        dummy->next = head;
        auto fast = dummy, slow = dummy;
        while (n--) fast = fast->next;
        
        while(fast->next)
        {
            fast = fast->next;
            slow = slow->next;
        }
        
        slow->next = slow->next->next;
        return dummy->next;
    }
};
```

