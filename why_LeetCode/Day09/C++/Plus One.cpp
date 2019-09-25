class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        add(digits,1);
        return digits;
    }

private:
void add(vector<int>& digits, int digit)
{
    int c=digit; //½øÎ»
    for(auto i=digits.rbegin();i!=digits.rend();i++)
    {
        *i+=c;
        c=*i/10;
        *i%=10;
    }

    if(c>0) digits.insert(digits.begin(),c);
}

};