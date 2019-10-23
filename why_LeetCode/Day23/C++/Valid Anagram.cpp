//����һ:�ֱ�����Ȼ��ȶ������ַ���
//ʱ�临�Ӷȣ�O(NlogN) �ռ临�Ӷȣ�O(1)
class Solution {
public:
    bool isAnagram(string s, string t) {
        sort(s.begin(),s.end());
        sort(t.begin(),t.end());
        return s==t;
    }
};

//������:ʹ�ù�ϣ�� �ֱ�ͳ�������ַ����ĸ����ַ����ֵĴ��� ���жԱ�
//ʱ�临�Ӷȣ�O(N) �ռ临�Ӷȣ�O(1)
class Solution {
public:
    bool isAnagram(string s, string t) {
       if(s.size()!=t.size())
            return false;

       unordered_map<char,int> map;
       for(int i=0;i<s.size();i++)
       {
            ++map[s[i]];
            --map[t[i]];
       }

       for(auto m:map)
       {
           if(m.second!=0)
            return false;
       }
       return true;
    }
};