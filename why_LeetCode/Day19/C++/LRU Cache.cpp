//采用哈希表方便查找
//采用双向链表方便插入删除
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
    
    //若不能找到key，返回-1；否则，将新访问的节点移到链表开头，同时更新哈希表中it
    int get(int key) {
        if(cacheMap.find(key)==cacheMap.end())
        {
            return -1;
        }

        cacheList.splice(cacheList.begin(),cacheList,cacheMap[key]);
        cacheMap[key]=cacheList.begin();
        return cacheMap[key]->value;
    }
    
    //若找不到key,则可以插入新值，同时检测链表是否到达最大容量，若达到，则删除表尾，同时更新哈希表，否则
    //在表头插入新值，更新哈希表；若找到key,则更新链表和哈希表
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