//时间：2019-9-25
//作者：fish_bot
//题目：LeetCode 42



//先扫描每个柱子左最大值（从1开始到结束）
//在扫描每个柱子右最大值（从倒数2开始到0）
//每个柱子左max和右max最小那个减去柱子高度=水个数
//计算列

class Solution {
public:
    int trap(vector<int>& height) {
        int len = height.size();
        vector<int> left(len),right(len);
        for(int i = 1; i<len; i++){
            left[i] = max(left[i-1],height[i-1]);
        }
        for(int i = len-2; i>=0; i--){
            right[i] = max(right[i+1],height[i+1]);
        }
        
        int res = 0;
        
        for(int i = 0; i < len; i++){
            int temp = min(left[i],right[i]);
            res += max(0,temp - height[i]);
        }
        return res;
    }
};


//用栈解，每个元素存储位置和高度，找到两个高墙之间的水面积
//计算行，所以要*宽度
class Solution {
public:
    int trap(vector<int>& height) {
        stack<pair<int,int>> s;
        int len = height.size();
        int res = 0;
        int h = 0;
        for(int i = 0; i<len; i++){
            while(!s.empty()){
                int right = s.top().first;
                int pos = s.top().second;
                res += (min(right,height[i]) - h) * (i-pos-1);
                h = right;
                
                if(height[i]<right)
                    break;
                else
                    s.pop();
            }
            s.push(make_pair(height[i],i));
        }
        return res;
    }
};
