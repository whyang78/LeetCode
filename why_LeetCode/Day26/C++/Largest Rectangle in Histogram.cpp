class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int max_area=0;
        stack<int> st;
        heights.push_back(0);
        for(int i=0;i<heights.size();)
        {
            if(st.empty() || heights[i]>heights[st.top()])
            {
                st.push(i++);
            }
            else
            {
                int temp=st.top();
                st.pop();
                max_area=max(max_area,
                        heights[temp]*(st.empty()?i:i-st.top()-1));
            }      
        }
        return max_area;
    }
};
