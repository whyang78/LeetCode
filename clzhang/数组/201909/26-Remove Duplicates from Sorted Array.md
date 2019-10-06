## 26 Remove Duplicates from Sorted Array（删除排序数组中的重复项）

给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

**示例 1:**

```
给定 nums = [1,1,1,2,2,3],

函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

你不需要考虑数组中超出新长度后面的元素。
```

排序数组，从头往后，若当前元素与前面相同，重复了，则不保存。

```c++
//2019/0916
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0; 
        int index = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[index] != nums[i])
                nums[++index] = nums[i];
        }
        return index+1;
    }
};

//
//
// class Solution {
// public:
//    int removeDuplicates(vector<int>& nums) {
//        if (nums.empty()) return 0;
//        int index = 1;
//        for (int i = 1; i < nums.size(); i++) {
//            if (nums[index-1] != nums[i])
//                nums[index++] = nums[i];
//        }
//        return index;
//    }
// };
//
// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
// for (int i = 0; i < len; i++) {
//     print(nums[i]);
// }

```



