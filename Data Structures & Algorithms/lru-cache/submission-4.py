class node():
    def __init__(self, key: int, val:int):
        self.key = key
        self.val = val

        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.d = {}
        self.c = capacity

        self.left, self.right = node(0, 0), node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def cleanup(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next = self.right
        node.prev = prev


    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]

            self.cleanup(node)
            self.insert(node)

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.cleanup(self.d[key])
        self.d[key] = node(key, value)
        self.insert(self.d[key])

        if len(self.d) > self.c:
            lru = self.left.next
            self.cleanup(lru)

            del self.d[lru.key]