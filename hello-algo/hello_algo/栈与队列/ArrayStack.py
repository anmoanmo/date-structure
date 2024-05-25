"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/5/25 19:16
@IDE:PyCharm
=============================
"""
class ArrayStack:
    def __init__(self):
        self._data = []
        self._size = 0

    def push(self, value):
        self._data.append(value)
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError('栈为空')
        else:
            self._size -= 1
            return self._data.pop()

    def peek(self):
        if self._size == 0:
            raise IndexError('栈为空')
        else:
            return self._data[-1]

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

if __name__ == '__main__':
    stack = ArrayStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.is_empty())
    print(stack.peek())
    print(stack.size())

