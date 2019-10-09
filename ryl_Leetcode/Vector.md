# Vector

Vector是C++标准库中的序列容器，它可以和数组一样可以高效的获取容器中的某个位置的元素，但是有一点是和数组不一样的，数组在定义完之后数组的大小就固定不变了，但是vector可以动态扩充内存。（需要注意的是：当vector的容量不足之后，vector会以一定的规则新建一个比原来vector更大的新容器，在将原来的元素都复制过去，所以有时候会使得效率比较低）



> 所以vector相对于数组来说，可以动态的管理内存，动态的扩大容量。相比于其他的容器比如deques、lists或者forward_lists，在容器的末尾添加和删除元素是非常的高效的。但是如果在容器中的中间位置插入一个元素的话效率相比原其他的容器就不是很适合。



**Vector是一个模板类，下面列举在刷题过程中经常使用的一些类方法：**

- **Iterators**: `begin() `  `end()`
- **Capacity**: `size()`  ` empty()`  ` capacity()`
- **Element access**: `[]`  `at`  `front`  `back`  
- **Modified**: `push_back`  `pop_back`  `insert` `erase`  `swap`



```cpp
#include<iostream>
#include<vector>

using namespace std;

int main()
{
    // 定义一个空的vector容器
    vector<int> myvector;

    cout << "is_empty:" << myvector.empty() << endl;

    // 从容器的末尾添加5个元素
    for(int i = 0; i < 5; i++)
        myvector.push_back(i);

    cout << "elements:" << endl;    
    // 显示容器中的内容
    for (int i = 0; i<5; i++)
        cout << myvector[i] << endl; 

    // 容器中元素的个数以及容器的最大容量
    cout << "size:" << myvector.size() << endl;
    cout << "capacity:" << myvector.capacity() << endl;

    // 获取容器中首末元素
    cout << "first element" << myvector.front() << endl;
    cout << "last element:" << myvector.back() << endl;

    // 在容器的第三个位置插入10
    cout << "insert 10 in the myvector[2]" << endl;
    myvector.insert(myvector.begin() + 2, 10);
    for (int i=0; i<myvector.size(); i++)
        cout << myvector[i] << endl;

    // erase 操作是左闭右开
    cout << "erase the element from myvector[1] to myvector[3]" << endl;
    myvector.erase(myvector.begin() + 1, myvector.begin() + 4);
    for (int i=0; i<myvector.size(); i++)
        cout << myvector[i] << endl;

    // 删除容器中最后一个元素
    cout << "remove the last element" << endl;
    myvector.pop_back();
    for (int i=0; i<myvector.size(); i++)
        cout << myvector[i] << endl;

    // 交换容器中的第一个和第二个元素
    cout << "swap the first element and the second one" << endl;
    swap(myvector[0], myvector[1]);
    for (int i=0; i<myvector.size(); i++)
        cout << myvector[i] << endl;

    // 使用.at访问元素
    cout << "using '.at' access elements" << endl;
    for (int i = 0; i< myvector.size(); i++) 
        cout << myvector.at(i) << endl;

    cout << "Test end" << endl;
    system("pause");
    return 0;
}
```



![1570167926551](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1570167926551.png)

