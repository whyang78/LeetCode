## 138 Copy List with Random Pointer（[复制带随机指针的链表](https://leetcode-cn.com/problems/Copy-List-with-Random-Pointer/)）

给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。

要求返回这个链表的深拷贝。 

 ![1570778548532](C:\Users\Administrator.PC-20190621JALE\AppData\Roaming\Typora\typora-user-images\1570778548532.png)

```
输入：
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

解释：
节点 1 的值是 1，它的下一个指针和随机指针都指向节点 2 。
节点 2 的值是 2，它的下一个指针指向 null，随机指针指向它自己。
```

### 两遍扫描，现将原节点逐个复制一遍，插在原节点后面，再扫描一遍，复制随即指针，注意，新节点的随机指针指向的应该是，原节点随即指针的下一个节点，因为原节点的下一个节点是自己的拷贝。

### 最后，拆分两个链表。

## Code

```C++
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (!head) return head;
        Node *p = head;
        while (head) {
            Node *tmp = new Node(head->val, nullptr, nullptr);
            tmp->next = head->next;
            head->next = tmp;
            head = tmp->next;
        }
        head = p;
        while (head) {
            if (head->random)
                head->next->random = head->random->next;
            head = head->next->next;
        }
        head = p;
        Node *res = head->next;
        Node *result = res;
        while (head) {
            head->next = head->next->next;
            head = head->next;
            if (res->next)
                res->next = res->next->next;
            res = res->next;
        }
        return result;
    }
};	
```

