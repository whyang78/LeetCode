class Solution {
public:
    void nextPermutation(vector<int>& nums) {
       //官方函数
       //next_permutation(nums.begin(),nums.end());
       my_next_permutation(nums.begin(),nums.end());
    }

private:
    template<typename it>
    bool my_next_permutation(it first, it last)
    {
        //反向迭代器
        const auto rfirst=reverse_iterator<it>(last);
        const auto rlast=reverse_iterator<it>(first);
        
        //寻找满足(a<b)的ab相邻数，找到a
        auto pivot=next(rfirst);
        while(pivot!=rlast && *pivot>=*prev(pivot))
        {
            pivot++;
        }

        //如果a已是反向末尾,则说明没有下一个排列
        if(pivot==rlast)
        {
            reverse(rfirst,rlast);
            return false;
        }
        
        //寻找自右边第一个大于a的值的位置
        auto change=find_if(rfirst,rlast,bind1st(less<int>(),*pivot));
        //交换
        swap(*change,*pivot);
        //逆序
        reverse(rfirst,pivot);
        return true;
    }
};
