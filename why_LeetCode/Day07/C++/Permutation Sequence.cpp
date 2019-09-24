//方法一：暴力求解法
//使用next_permutation
class Solution {
public:
    string getPermutation(int n, int k) {
        string s(n,'0');
        for(int i=0;i<n;i++)
            s[i]+=i+1;
        
        for(int i=0;i<k-1;i++)
            next_permutation(s.begin(),s.end());
        return s;
    }
};


//方法二：康托编码
class Solution {
public:
    string getPermutation(int n, int k) {
        string s(n,'0');
        for(int i=0;i<n;i++)
            s[i]+=i+1;
        return kth_Permutation(s,k);
    }

private:
    int factorial(int n)
    {
        int result=1;
        for(int i=1;i<=n;i++)
        {
            result*=i;
        }
        return result;
    }

    template<typename sequence>
    sequence kth_Permutation(sequence& seq,int k)
    {
        sequence s(seq);
        sequence result;
        int n=seq.size();

        int base=factorial(n-1);
        k--;

        for(int i=n-1;i>0;k%=base,base/=i,i--)
        {
            auto a=next(s.begin(),k/base);
            result.push_back(*a);
            s.erase(a);
        }

        result.push_back(s[0]);
        return result;
    }
};
