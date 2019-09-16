//2019/0915
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
