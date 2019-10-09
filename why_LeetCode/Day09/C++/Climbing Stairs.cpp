//递归，超时
class Solution {
public:
    int climbStairs(int n) {
        return fac(n);
    }

private:
    int fac(int n)
    {
        if(n==1||n==2)
            return n;
        else
            return fac(n-1)+fac(n-2);
    } 
};

//迭代
class Solution {
public:
    int climbStairs(int n) {
        int cur=1; //当前值
        int pre=0; //前一个值
        for(int i=1;i<=n;i++)
        {
            int temp=cur;
            cur+=pre;
            pre=temp;
        }

        return cur;
    }
};


//数学公式
//斐波那契数列  a1=1 a2=1 a3=2  所以n要加一 使得1层对应a2,2层对应a3
class Solution {
public:
int climbStairs(int n) {
    const double s = sqrt(5);
    return floor((pow((1+s)/2, n+1) + pow((1-s)/2, n+1))/s + 0.5);
    }
};