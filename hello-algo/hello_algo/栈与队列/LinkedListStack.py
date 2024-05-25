"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/5/25 15:38
@IDE:PyCharm
=============================
"""
# class LinkedListStackNode:
#     def __init__(self, value=0, next_node=None):
#         self.value = value
#         self.next = next_node
#
# class LinkedListStack:
#     def __init__(self):
#         self.head = None
#
#     def push(self, value):
#         new_node = LinkedListStackNode(value, self.head)
#         self.head = new_node
#
#     def pop(self):
#         if self.head is None:
#             return None
#         else:
#             pop_value = self.head.value
#             self.head = self.head.next
#             return pop_value
#
#     def peek(self):
#         if self.head is None:
#             return None
#         else:
#             return self.head.value
#
#     def is_empty(self):
#         return self.head is None
#
#
# if __name__ == '__main__':
#     stack = LinkedListStack()
#     stack.push(1)
#     stack.push(2)
#     stack.push(3)
#
#     print("Peek:", stack.peek())
#     print("Pop:", stack.pop())
#     print("Peek after pop:", stack.peek())

class LinkedListStackNode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedListStack:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def push(self, value):
        node = LinkedListStackNode(value, self.head)
        self.head = node
        if self.tail is None:
            self.tail = node
        self.size += 1

    def pop(self):
        if self.head:
            pop_value = self.head.value
            self.head = self.head.next
            self.size -= 1
            if self.head == None:
                self.tail = None
            return pop_value
        else:
            return None

    def peek(self):
        return self.head.value

    def is_empty(self):
        return self.head is None


if __name__ == '__main__':
    stack = LinkedListStack()
    print("isempty =", stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("isempty =", stack.is_empty())
    print('size =', stack.size)
    print("Peek:", stack.peek())
    print('size =', stack.size)
    print('tail =', stack.tail.value)
    print("Pop:", stack.pop())
    print("Peek after pop:", stack.peek())



