## 26. Remove Duplicates from Sorted Array

**题目描述：**给定一个排序数组，移除数组中重复的元素，空间复杂度要求为O(1)

**解题思路：**引入一个标记变量，该标记变量用来记录数组中最终保留下的最新的元素的位置。该变量初始化为0位置，从1位置开始遍历整个数组。当array[i]!=array[index]时，index和i一起往后移动，需要注意的是array[i]的值应该是index+1位置上面的值，因为i在index的前面（这也是最后返回的时候是index+1，而不是index的原因）。如果相等，只移动i。只移动i相当于把重复的元素给略过了。

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty())  return 0; 
        
        int index = 0;
        for (int i = 1; i<nums.size(); i++)
        {
            if(nums[index] != nums[i])
                nums[++index] = nums[i];
        }
        return index + 1; 
    }
};
```

## 80. Remove Duplicates from Sorted Array II 

**题目描述：**与Remove Duplicates from Sorted Array基本是一样的，只不过这里允许最多重复的数字为2

**结题思路：**结题思路也与I很相似，只不过这里需要在I的基础上在引入一个变量来记录重读的次数。这里最多允许有两个重复，言下之意就是在代码实现的时候最多只允许跳过一次重复的数。这里可以继续扩展到最多允许3个或者n个重复数字，在代码实现的时候就是允许跳过n-1次重复的数字，在这之后只能如果还出现重复的数字，那么就应该将循环变量往后面移动，将多余的重复的数字去掉。

```cpp
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size()<2) return nums.size();
        
        int len = nums.size();
        int count = 1;
        int index = 0;
        for (int i=1; i<len; i++)
        {
            if(nums[index] == nums[i] && count<2)
            {
                count++;
                nums[++index] = nums[i];
            }
            else if(nums[index] != nums[i])
            {
                count = 1;
                nums[++index] = nums[i];
            }
        }
        
        return index+1;
    }
};
```

## 33.Search in Rotated Sorted Array

**题目描述：**

![1568647249065](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1568647249065.png)

**解题思路：**

首先题目中给出的是一个升序序列并且没有重复数字，然后一某一个基准元素进行旋转，旋转之后被分成了两端但是每一段上还是递增的。我们知道当序列是有序的时候一般会使用二分查找的方法去找元素，这样速度比较快，并且时间复杂度是O(logn)。但是对于这种不是完全有序的序列如何进行查找呢？首先我们会发现一个规律，当旋转之后的序列如果中间值小于最右边的值，则中间值右边的部分肯定是递增的，如果中间值大于最后面的值，说明中间值的左半部分肯定是递增的，下面举个例子：

原始数组：[1, 2, 4, 5, 7, 9 ]

旋转后的数组：[5, 7, 9, 1, 2, 4] (此时中间值大于最右边值)

旋转后的数组：[7, 9, 1, 2, 4, 5] (此时中间值小于最右边值)

基于这种发现，我们可以用二分查找的方法解决这个问题.

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        // 通过上面的初始值可以知道，while循环的条件需要取等号，搜索区间为：[l,r]
        while( l<=r )
        {
            // >>1表示的是除以2
            int mid = l + ((r - l)>>1);
            if(nums[mid] == target) return mid;
            // nums[mid] < nums[r] 说明mid左边的元素是升序的
            if(nums[mid] < nums[r])  
            {   
                //但是还需要进一步确定target是否在右边这个范围内，如果在的话就直接使用二分查找缩小范围
                if(target > nums[mid] && target <= nums[r])
                {
                    l = mid + 1;    
                }
                else  // 当target不在左边的升序序列中时，mid往反方向进行缩减
                {
                    r = mid - 1;
                }
            }
            else 
            {
                if (target >= nums[l] && target < nums[mid])
                {
                    r = mid - 1;
                }
                else
                {
                    l = mid + 1;
                }
            }
        }
        
        return -1;
    }
};
```

## 81. Search in Rotated Sorted Array II

**题目描述：**

![1568647868415](C:\Users\ryLuo\AppData\Roaming\Typora\typora-user-images\1568647868415.png)

**解题思路：**

该题再30题的基础上去掉了没有重复元素的约束，其实我们可以发现当有重复元素，但是旋转的时候没有在重复元素中间进行旋转的话，相当于重复的元素没有散开还是连在一起也可以认为是升序的，此时用30题中的方法（中间值小于最右边的值，则右半段是递增的，中间值小于最右边的值则左半段是递增的，此时没有重复数字所以没有等于的情况）仍然可以通过。那么如果在重复数字中间进行旋转会出现什么情况呢？下面通过一个例子进行说明：

原始数组：[1 1 1 1 1 5]

旋转后的数组：[1 5 1 1 1 1]

旋转后的数组：[1 1 1 1 5 1]

上面是随便举的例子，当数组在重复数字中间进行旋转，可能有上述的两种结果（当然还有其他的很多种结果），但是我们会发现当出现这种情况，只有一种现象出现，那就是中间的值等于最右边的值，此时上述两种情况都能说明这件事情，并且通过上述的这两种情况我们会发现此时我们无法判断数组在哪一边是递增的（二分查找只能对有序序列进行查找）。此时我们相比于30题时多了一种判断，那就是如果中间值等于右边值的时候的处理方法。既然当中间值等于最右边值的时候我们无法进行判断，我们可以让右边的位置往前面移动一个，直到不相等的时候，此时右半段就是递增的，可以用二分搜索进行查找。

注意：由于第30题，用的是将中间值与最右边值进行比较，所以这里也采用这种比较的方法，也可以将中间的值与最左边的值进行比较，具体的操作就基本相反了。

```cpp
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        while( l<=r )
        {
            int mid = l + ((r-l)>>2);
            
            if(nums[mid] == target) return true;
            
            if(nums[mid] < nums[r])
            {
                
                if(target > nums[mid] && target <= nums[r])
                {
                    l = mid + 1;
                }
                else
                {
                    r = mid - 1; 
                }
            }
            else if(nums[mid] > nums[r])
            {
                if(target >= nums[l] && target < nums[mid])
                {
                    r = mid - 1;
                }
                else
                {
                    l = mid + 1;
                }
            }
            else  //此时中间值等于最右边值
            {
                r--;
            }
        }
        return false;
    }
};
```

