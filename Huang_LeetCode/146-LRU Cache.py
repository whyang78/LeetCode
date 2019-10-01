class LRUCache:
    def __init__(self, capacity: int):
        self.od, self.cap = collections.OrderedDict(), capacity

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            del self.od[key]
        elif len(self.od) == self.cap:
            self.od.popitem(False)  # 先进先出
        self.od[key] = value