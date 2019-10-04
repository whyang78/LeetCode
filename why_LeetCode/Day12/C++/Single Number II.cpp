//方法一：
//位运算，之前使用异或操作，实质上是位运算满足0+0=0，0+1=1，1+1=0(不进位的二进制运算)；
//在此题中，需满足0+1=1，1+1=2，1+2=0(不进位的三进制运算)；
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        const int n=sizeof(int)*8;
        vector<int> count(n,0);
        int result=0;

        for(int i=0;i<nums.size();i++)
        {
            for(int j=0;j<n;j++)
            {
                count[j]+=(nums[i]>>j)& 1;
                count[j]%=3;
            }
        }
        for(int j=0;j<n;j++)
        {
            result+=(count[j]<<j);
        }
        return result;
    }
};


//方法二：
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int ones=0, twos=0, threes=0;
        for (auto num : nums)
        {
            twos |= ones & num; // 二进制某位出现1次时twos = 0，出现2, 3次时twos = 1；
            ones ^= num;  // 二进制某位出现2次时ones = 0，出现1, 3次时ones = 1；
            threes = ones&twos ;// 二进制某位出现3次时（即twos = ones = 1时）three = 1，其余即出现1, 2次时three = 0；
            ones &= ~threes; //将二进制下出现3次的位置零，实现`三进制下不考虑进位的加法`；
            twos &= ~threes;
        }
        return ones;
    }
};