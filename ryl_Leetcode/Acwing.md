# Acwing

## 1. 快速排序

![image-20191031092908616](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\image-20191031092908616.png)

```cpp
#include <iostream>
using namespace std;

const int N = 100010;
int q[N];

void quick_sort(int q[], int l, int r)
{
    if(l >= r) return;
    
    // 确定分界点，为了不出现边界问题，取分界点的时候每次都取中间的点
    int i = l - 1, j = r + 1, x = q[l + r >> 1]; 
    
    while(i < j)
    {
        // 边界点左边元素的值都小于等于边界点的值
        // 边界点右边元素的值都大于等于边界点的值
        do i++; while(q[i] < x);
        do j--; while(q[j] > x);
        if(i < j) swap(q[i], q[j]);
    }
    
    // 递归排序边界点左边和右边的元素
    quick_sort(q, l, j);
    quick_sort(q, j + 1, r);
}

int main()
{
    int n; 
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++) scanf("%d", &q[i]);
    
    quick_sort(q, 0, n - 1);
    
    for(int i = 0; i < n; i++) printf("%d ", q[i]);
    
    return 0;
}
```

快排模板：

```cpp
void quick_sort(int q[], int l, int r)
{
    if(l >= r) return;
    
    // 确定分界点，为了不出现边界问题，取分界点的时候每次都取中间的点
    int i = l - 1, j = r + 1, x = q[l + r >> 1]; 
    
    while(i < j)
    {
        // 边界点左边元素的值都小于等于边界点的值
        // 边界点右边元素的值都大于等于边界点的值
        do i++; while(q[i] < x);
        do j--; while(q[j] > x);
        if(i < j) swap(q[i], q[j]);
    }
    
    // 递归排序边界点左边和右边的元素
    quick_sort(q, l, j);
    quick_sort(q, j + 1, r);
}
```

## 2. 第K小的数

![image-20191031094007649](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\image-20191031094007649.png)

```cpp
#include <iostream>
using namespace std;

const int N = 100010;
int q[N];

int quick_sort(int q[], int l, int r, int k)
{
    if(l >= r) return q[l];
    
    int i = l - 1, j = r + 1, x = q[l + r >> 1];
    
    while(i < j)
    {
        do i++; while(q[i] < x);
        do j--; while(q[j] > x);
        if(i < j) swap(q[i], q[j]);
    }
    
    // 判断第K个数是在分界点的左半边还是右半边
    if (j - l + 1 >= k) return quick_sort(q, l, j, k);
    else return quick_sort(q, j + 1, r, k - (j - l + 1));
}

int main()
{
    int n, k;
    scanf("%d%d", &n, &k);
    
    for(int i = 0; i < n; i++) scanf("%d", &q[i]);
    
    cout << quick_sort(q, 0, n - 1, k) << endl;
    
    return 0;
}
```

## 3. 归并排序

![image-20191101195803176](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\image-20191101195803176.png)

```cpp
#include <iostream>
using namespace std;

const int N = 100010;
int q[N], temp[N];

void merge_sort(int q[], int l, int r)
{
    if(l >= r) return;
    int mid = l + r >> 1;

    merge_sort(q, l, mid), merge_sort(q, mid + 1, r);
    
    int i = l, j = mid + 1, k = 0;
    while(i <= mid && j <= r)
    {
        if(q[i] <= q[j]) temp[k++] = q[i++];
        else temp[k++] = q[j++];
    }
    
    while(i <= mid) temp[k++] = q[i++];
    while(j <= r) temp[k++] = q[j++];
    
    for(i = l, j = 0; i <= r; i++, j++) q[i] = temp[j];
}

int main()
{
    int n;
    scanf("%d", &n);
    
    for(int i = 0; i < n; i++) scanf("%d", &q[i]);
    
    merge_sort(q, 0, n - 1);
    
    for(int i = 0; i < n; i++) printf("%d ", q[i]);
    
    return 0;    
}
```

## 4. 逆序对的数量

![image-20191101202339728](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\image-20191101202339728.png)

```cpp
#include <iostream>
typedef long long LL;

using namespace std;
const int N = 100010;
int q[N], tmp[N];

LL merge_sort(int l, int r)
{
    if(l >= r) return 0;
    
    int mid = l + r >> 1;
    // 求分界点左边和右边的逆序对
    LL res = merge_sort(l, mid) + merge_sort(mid + 1, r);
    
    int k = 0, i = l, j = mid + 1;
    while(i <= mid && j <= r)
    {
        // 逆序对的定义
        if(q[i] <= q[j]) tmp[k++] = q[i++];
        else
        {
            // 求逆序对分布在归并的数组的左右两边
            tmp[k++] = q[j++];
            res += mid - i + 1;
        }
    }
    
    while(i <= mid) tmp[k++] = q[i++];
    while(j <= r) tmp[k++] = q[j++];
    
    // 将排序好的元素放回原始数组中 i的范围是从l~r
    for(i = l, j = 0; i <= r; i++, j++) q[i] = tmp[j];
    return res;
}

int main()
{
    int n;
    scanf("%d", &n);
    
    for(int i = 0; i < n; i ++) scanf("%d", &q[i]);
    
    cout << merge_sort(0 ,n - 1) << endl;
    
    return 0;
}
```



