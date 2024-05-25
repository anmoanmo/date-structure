"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/5/25 20:13
@IDE:PyCharm
=============================
"""
class LinkedListDequeNode:
    def __init__(self, value=None, before=None, after=None):
        self.value = value
        self.before: LinkedListDequeNode | None = before
        self.after: LinkedListDequeNode | None = after

class LinkedListDeque(object):
    def __init__(self):
        self.head: LinkedListDequeNode | None = None
        self.tail: LinkedListDequeNode | None = None
        self.size = 0

    def push_back(self, value):
        node = LinkedListDequeNode(value=value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.after = node
            node.before = self.tail
            self.tail = node
        self.size += 1

    def push_front(self, value):
        node = LinkedListDequeNode(value=value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.before = node
            node.after = self.head
            self.head = node
        self.size += 1

    def pop_front(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.after
        if self.head is not None:
            self.head.before = None
        else:
            self.tail = None  # 处理只有一个节点的情况
        self.size -= 1
        return node.value

    def pop_back(self):
        if self.tail is None:
            return None
        node = self.tail
        self.tail = self.tail.before
        if self.tail is not None:
            self.tail.after = None
        else:
            self.head = None  # 处理只有一个节点的情况
        self.size -= 1
        return node.value

    def get_size(self):  # 方法名从 size 改为 get_size
        return self.size

    def is_empty(self):
        return self.head is None

    def peek_front(self):
        if self.head is None:
            return None
        return self.head.value

    def peek_back(self):
        if self.tail is None:
            return None
        return self.tail.value


if __name__ == '__main__':
    ld = LinkedListDeque()
    ld.push_back(1)
    ld.push_back(2)
    ld.push_back(3)
    ld.push_back(4)
    ld.push_back(5)
    print(ld.is_empty())
    print(ld.pop_front())
    print(ld.pop_back())
    print(ld.peek_front())
    print(ld.peek_back())
    print(ld.is_empty())
    print(ld.get_size())  # 更改为 get_size
