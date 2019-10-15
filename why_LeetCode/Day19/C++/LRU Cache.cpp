//���ù�ϣ�������
//����˫�����������ɾ��
class LRUCache {
private:
    struct cacheNode
    {
        int key;
        int value;
        cacheNode(int k,int v):key(k),value(v){};
    };
    list<cacheNode> cacheList;
    unordered_map<int,list<cacheNode>::iterator> cacheMap;
    int capacity;
    
public:
    LRUCache(int capacity) {
        this->capacity=capacity;
    }
    
    //�������ҵ�key������-1�����򣬽��·��ʵĽڵ��Ƶ�����ͷ��ͬʱ���¹�ϣ����it
    int get(int key) {
        if(cacheMap.find(key)==cacheMap.end())
        {
            return -1;
        }

        cacheList.splice(cacheList.begin(),cacheList,cacheMap[key]);
        cacheMap[key]=cacheList.begin();
        return cacheMap[key]->value;
    }
    
    //���Ҳ���key,����Բ�����ֵ��ͬʱ��������Ƿ񵽴�������������ﵽ����ɾ����β��ͬʱ���¹�ϣ������
    //�ڱ�ͷ������ֵ�����¹�ϣ�����ҵ�key,���������͹�ϣ��
    void put(int key, int value) {
        if(cacheMap.find(key)==cacheMap.end())
        {
            if(cacheList.size()==capacity)
            {
                cacheMap.erase(cacheList.back().key);
                cacheList.pop_back();
            }
            cacheList.push_front(cacheNode(key,value));
            cacheMap[key]=cacheList.begin();
        }
        else
        {
            cacheMap[key]->value=value;
            cacheList.splice(cacheList.begin(),cacheList,cacheMap[key]);
            cacheMap[key]=cacheList.begin();
        }
    }
};