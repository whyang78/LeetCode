//方法一：使用数学公式 
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result;
        const int num=1<<n;
        result.reserve(num);

        for(int i=0;i<num;i++)
        {
            result.push_back(bin2gray(i));
        }
        return result;
    }

private:
    int bin2gray(int n)
    {
        return n^(n>>1);
    }
};

//方法二：迭代
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result;
        const int num=1<<n;
        result.reserve(num);
        result.push_back(0);

        for(int i=0;i<n;i++)
        {
            int highest_bit=1<<i;
            for(int j=result.size()-1;j>=0;j--)
            {
                result.push_back(highest_bit|result[j]);
            }
        }
        return result;
    }
};