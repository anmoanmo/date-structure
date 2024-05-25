"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/5/25 20:00
@IDE:PyCharm
=============================
"""
class ArrayQueue:
    def __init__(self):
        self.items = []

    def enqueue(self,value):
        self.items.append(value)

    def dequeue(self):
        head_value = self.items[0]
        self.items = self.items[1:]
        return head_value

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self): return len(self.items)

if __name__ == '__main__':
    ll = ArrayQueue()
    print(ll.is_empty())
    ll.enqueue(1)
    ll.enqueue(2)
    ll.enqueue(3)
    ll.enqueue(4)
    print(ll.peek())
    print(ll.dequeue())
    print(ll.dequeue())
    print(ll.peek())

    print(ll.is_empty())
    print(ll.size())
