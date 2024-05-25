"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/5/25 19:39
@IDE:PyCharm
=============================
"""
class LinkedListQueueNode:
    def __init__(self, value=None, before=None, after=None):
        self.value = value
        self.before = before
        self.after = after

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        if self.head is None:
            self.head = LinkedListQueueNode(value)
            self.tail = self.head
            self.size += 1
        else:
            node = LinkedListQueueNode(value)
            self.tail.after = node
            node.before = self.tail
            self.tail = node
            self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            self.head = self.head.after
            self.head.before = None
            self.size -= 1
            return value

    def peek(self):
        if self.head is None:
            return None
        else:
            return self.head.value

    def is_empty(self):
        return self.size == 0


if __name__ == '__main__':
    ll = LinkedListQueue()
    print(ll.head)
    print(ll.is_empty())
    ll.enqueue(1)
    ll.enqueue(2)
    ll.enqueue(3)
    ll.enqueue(4)
    print(ll.peek())
    print(ll.dequeue())
    print(ll.dequeue())
    print(ll.is_empty())
    print(ll.size)

