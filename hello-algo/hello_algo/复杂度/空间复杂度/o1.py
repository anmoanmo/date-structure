"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/5/20 15:03
@IDE:PyCharm
=============================
"""
from typing import Optional


class ListNode(object):
    def __init__(self, val: int):
        self.val: int = val
        self.next: Optional[ListNode] = None
def function() -> int:
    """函数"""
    # 执行某些操作
    return 0

def constant(n: int):
    """常数阶"""
    # 常量、变量、对象占用 O(1) 空间
    a = 0
    nums = [0] * 10000
    node = ListNode(0)
    # 循环中的变量占用 O(1) 空间
    for _ in range(n):
        c = 0
    # 循环中的函数占用 O(1) 空间
    for _ in range(n):
        function()