class Solution {
public:
    bool isNumber(string s) {
        return isnumber(s.c_str());
    }
private:
    bool isnumber(const char *s)
    {
        char *st;
        strtod(s,&st);
        if(st==s) return false;
        for(;*st;st++)
        {
            if(!isspace(*st))
            {
                return false;
            }
        }
        return true;
    }
};