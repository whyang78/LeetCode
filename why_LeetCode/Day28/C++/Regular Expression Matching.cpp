class Solution {
public:
    bool isMatch(string s, string p) {
        return ismatch(s.c_str(),p.c_str());
    }
private:
    bool ismatch(const char* s,const char* p)
    {
        if(*p=='\0') return *s=='\0';

        if(*(p+1)!='*')
        {
            if(*p==*s || (*p=='.'&&*s!='\0'))
            {
                return ismatch(s+1,p+1);
            }
            else
            {
                return false;
            }
        }
        else
        {
            while(*p==*s || (*p=='.'&&*s!='\0'))
            {
                if(ismatch(s,p+2))
                {
                    return true;
                }
                s++;
            }
            return ismatch(s,p+2);
        }    
    }
};