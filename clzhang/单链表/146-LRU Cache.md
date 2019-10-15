## 146 LRU Cache（[ LRU缓存机制](https://leetcode-cn.com/problems/LRU-Cache/)）

运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。

进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？

**示例:**

```
LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
```

要求\mathcal{O}(1)复杂度，用双向链表，和哈希表，哈希表来存储key及对应的迭代器地址，搜索key是否存在以及获得迭代器地址值时的复杂度为\mathcal{O}(1)；

获取数据get(key)，根据哈希表中存的秘钥key对应的迭代器地址去读取存储的数据，数据存储在一个双向链表cacheList中，根据迭代器地址读取数据的复杂度为\mathcal{O}(1)，实现最近最少访问时，需要每次访问某个秘钥时，将其对应的节点移动至链表最前端\mathcal{O}(1)，这样使链表最后的优先级最低，若缓存满，移除的就是链表末尾节点。

```C++
class LRUCache {
private:
	struct CacheNode {
		int key;
		int value;
		CacheNode(int k, int v) : key(k), value(v) {}
	};
	list<CacheNode> cacheList;
	unordered_map<int, list<CacheNode>::iterator> cacheMap;
	int capacity;
public:
	LRUCache(int capacity) {
		this->capacity = capacity;
	}
	int get(int key) {
		if (cacheMap.find(key) == cacheMap.end()) return -1;    //没有秘钥key，返回-1
		cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);  //有，最近访问，移至最前端
		cacheMap[key] = cacheList.begin();
		return cacheMap[key]->value;    //返回数据
	}
	void put(int key, int value) {
		if (cacheMap.find(key) == cacheMap.end()) {	//缓存中没有该秘钥
			if (cacheList.size() == capacity) {	//若缓存满
				cacheMap.erase(cacheList.back().key);	//删除最后一个节点
				cacheList.pop_back();
			}
			cacheList.push_front(CacheNode(key, value));    //最近访问，存于链表最前端
			cacheMap[key] = cacheList.begin();
		}
		else {	//有该秘钥
			cacheMap[key]->value = value;	//更新秘钥值
            //最近访问，移至链表最前端
			cacheList.splice(cacheList.begin(), cacheList, cacheMap[key]);
			cacheMap[key] = cacheList.begin();
		}
	}
};
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```

