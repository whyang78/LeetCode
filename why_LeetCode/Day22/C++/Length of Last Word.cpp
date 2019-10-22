class Solution {
public:
    int lengthOfLastWord(string s) {
        auto first=find_if(s.rbegin(),s.rend(),::isalpha);
        auto last=find_if_not(first,s.rend(),::isalpha);
        return distance(first,last);
    }
};

class Solution {
public:
    int lengthOfLastWord(string s) {
        int length=0;
        int i=s.size()-1;
        
        while(s[i]==' ') {i--;}

        while(i>=0&&s[i]!=' ')
        {
            length++;
            i--;
        }
        
        return length;
    }
};