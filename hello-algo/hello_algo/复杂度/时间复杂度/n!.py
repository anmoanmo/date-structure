"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/5/20 14:52
@IDE:PyCharm
=============================
"""
def factorial_recur(n: int) -> int:
    """阶乘阶（递归实现）"""
    if n == 0:
        return 1
    count = 0
    # 从 1 个分裂出 n 个
    for _ in range(n):
        count += factorial_recur(n - 1)
    return count