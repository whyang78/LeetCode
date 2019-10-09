//方法一：暴力求解法 
//对于数组中的每个元素，我们找出下雨后水能达到的最高位置，等于两边最大高度的较小值减去当前高度的值。
//时间复杂度：O(N2) 空间复杂度：O(1)
class Solution {
public:
    int trap(vector<int>& height) {
        const int n=height.size();
        int ans=0;

        for(int i=1;i<n-1;i++)
        {
            int max_left=0,max_right=0;
            for(int j=i;j>=0;j--)
            {
                max_left=max(max_left,height[j]);
            }
            for(int j=i;j<n;j++)
            {
                max_right=max(max_right,height[j]);
            }
            ans+=min(max_left,max_right)-height[i];
        }
        return ans;
    }
};


//方法二：动态规划 
//提前存储max。因此，可以通过动态编程解决
//时间复杂度：O(N) 空间复杂度：O(N)
class Solution {
public:
    int trap(vector<int>& height) {
        if(height.empty())
            return 0;

        const int n=height.size();
        int ans=0;
        vector<int> max_left(n),max_right(n);

        max_left[0]=height[0];
        max_right[n-1]=height[n-1];
        for(int i=1;i<n;i++)
        {
            max_left[i]=max(max_left[i-1],height[i]);
            max_right[n-i-1]=max(max_right[n-i],height[n-i-1]);
        }
        for(int i=0;i<n;i++)
        {
            ans+=min(max_left[i],max_right[i])-height[i];
        }

        return ans;
    }
};

//方法三：以最高划分成两部分，分别运算 
//时间复杂度：O(N) 空间复杂度：O(1)
class Solution {
public:
    int trap(vector<int>& height) {
        if(height.empty())
            return 0;
            
        const int n=height.size();
        int m=0;
        for(int i=0;i<n;i++)
        {
            if(height[i]>height[m])
                m=i;
        }

        int ans=0;
        for(int i=0,top=0;i<m;i++)
        {
            if(height[i]>top) 
                top=height[i];
            else
                ans+=top-height[i];
        }

        for(int i=n-1,top=0;i>m;i--)
        {
            if(height[i]>top)
                top=height[i];
            else
                ans+=top-height[i];
        }

        return ans;
    }
};

//方法四：栈
//如果当前的条形块小于或等于栈顶的条形块，我们将条形块的索引入栈，意思是当前的条形块被栈中的前一个条形块界定。
//如果我们发现一个条形块长于栈顶，我们可以确定栈顶的条形块被当前条形块和栈的前一个条形块界定，因此我们可以弹出栈顶元素并且累加答案到ans。
//时间复杂度：O(N) 空间复杂度：O(N)
class Solution {
public:
    int trap(vector<int>& height) {
        if(height.empty())
            return 0;

        const int n=height.size();
        int ans=0;
        int current=0;
        stack<int> st;
        while(current<n)
        {
            while(!st.empty() && height[current]>height[st.top()])
            {
                int top=st.top(); //原top  一会要pop
                st.pop();
                if(st.empty())
                    break;

                //height[st.top()] height[top] height[current]形成沟壑
                int distance=current-st.top()-1; //现top
                int bounded_height=min(height[current],height[st.top()])-height[top];
                ans+=distance*bounded_height;
            }
            st.push(current++);
        }
        return ans;
    }
};