//方法一：一次遍历 时间复杂度:O(n2)
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        const int num=gas.size();
        bool flag;
        for(int i=0;i<num;i++)
        {
            int j=i;
            int total_cost=0,total_gas=0;
            flag=false;
            while(1)
            {
                total_gas+=gas[j];
                total_cost+=cost[j];
                if(total_gas>=total_cost)
                {
                    j++;
                    j%=num;
                    if(j==i)
                        break;
                }
                else
                {
                    flag=true;
                    break;
                }
            }
            
            if(!flag)
                return j;            
        }
        
        if(flag)
            return -1;
        
        return 0;
    }
};

//方法二:时间复杂度 O(N) 空间复杂度 O(1)
//首先要知道能走完整个环的前提是gas的总量要大于cost的总量，这样才会有起点的存在。
//假设开始设置起点start = 0, 并从这里出发，如果当前的gas值大于cost值，就可以继续前进，
//此时到下一个站点，剩余的gas加上当前的gas再减去cost，看是否大于0，若大于0，则继续前进。
//当到达某一站点时，若这个值小于0了，则说明从起点到这个点中间的任何一个点都不能作为起点，
//则把起点设为下一个点，继续遍历。当遍历完整个环时，当前保存的起点即为所求。
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total = 0;
        int j = 0;
        for (int i = 0, sum = 0; i < gas.size(); i++) 
        {
            sum += gas[i] - cost[i];
            total += gas[i] - cost[i];
            if (sum < 0) {
                j = i+1;
                sum = 0;
                }
        }
        return total >= 0 ? j : -1;

    }
};
