# Stack

## 155. Min Stack

![1571731202313](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571731202313.png)

解题思路：

这道题的意思是，自己实现一个栈，这个栈不仅拥有正常栈的功能，并且还可以以常数的复杂度随时返回栈中的最小值，也就是在自己创建的栈中需要维护一个栈的最小值，这里可以使用两个栈，一个是正常功能的栈，另外一个是维护栈顶元素为栈的最小值，也就是如果push进来的值小于等于栈顶元素，才将其push进来，否则不进行push。

```cpp
class MinStack {
public:
    stack<int> s1, s2;
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        s1.push(x);
        if (s2.empty() || s2.top() >= x) s2.push(x); 
    }
    
    void pop() {
        if(s2.top() == s1.top()) s2.pop();
        s1.pop();
    }
    
    int top() {
        return s1.top();
    }
    
    int getMin() {
        return s2.top();        
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```

## 225. Implement Stack using Queue

![1571731422323](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571731422323.png)

解题思路：

这题的主要意思是使用队列来实现一个栈，首先需要回顾一下队列与栈的特性。栈是先进后出,队列是后进先出。所以我们每次往队列push完一个元素之后都将，整个队列中的元素从头在查到尾部，直到刚插入的元素到队列的头部，其他的操作就和正常的stack是一样的。

不过需要注意的是：C++标准库中获取栈顶元素是stack.top(), 而对于队列是queue.front()

```cpp
class MyStack {
public:
    queue<int> q;
    /** Initialize your data structure here. */
    MyStack() {
        
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        q.push(x);
        for(int i = 0; i < q.size() - 1; i++) 
            q.push(q.front()), q.pop();
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int res = q.front();
        q.pop();
        return res;
    }
    
    /** Get the top element. */
    int top() {
        return q.front();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return q.empty();
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
```

## 232. Implement Queue using Stacks

![1571731839130](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1571731839130.png)

解题思路：

这一题是使用栈来实现队列，上面一个题时用队列实现栈，我们可以在push一个元素之后，在将所有的队列的元素重新按顺序从头部查到尾部，直到刚在尾部插入的新元素到达队列的头部。但是这里使用栈来实现队列就不一样了，因为栈的一边是封闭的，不能那么做，这里的做法是使用两个栈来实现一个队列。一个栈只用来push元素，另一个栈只用来pop，以及top元素。具体实现就是push元素的时候不需要考虑任何情况直接往第一个栈中push就行，当需要获取自定义队列的元素或者pop元素的时候，首先判断第二个stack是否为空，如果为空就将第一个栈中的元素意思pop进第二个栈中，这样就实现了元素顺序的反转。如果第二个栈中还有元素就可以直接进行top 和pop操作。

```cpp
class MyQueue {
public:
    stack<int> s1, s2;
    /** Initialize your data structure here. */
    MyQueue() {
        
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        s1.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if (s2.empty())
            while(s1.size())
                s2.push(s1.top()), s1.pop();
        
        int res = s2.top();
        s2.pop();
        return res;
    }
    
    /** Get the front element. */
    int peek() {
        if (s2.empty())
            while(s1.size())
                s2.push(s1.top()), s1.pop();
        
        return s2.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return s1.empty() && s2.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
```





