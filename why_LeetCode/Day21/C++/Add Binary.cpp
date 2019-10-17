class Solution {
public:
    string addBinary(string a, string b) {
        string result;
        const int n=a.size()>b.size()?a.size():b.size();
        reverse(a.begin(),a.end());
        reverse(b.begin(),b.end());
        
        int carry=0;
        for(int i=0;i<n;i++)
        {
            int ai=i<a.size()?(a[i]-'0'):0;
            int bi=i<b.size()?(b[i]-'0'):0;
            int ci=(ai+bi+carry)%2;
            carry=(ai+bi+carry)/2;
            result.insert(result.begin(),(ci+'0'));
        }
        if(carry)
        {
            result.insert(result.begin(),(carry+'0'));
        }
        return result;
    }
};