"""
=============================
ᕕ(◠ڼ◠)ᕗ
@time:2024/5/20 14:52
@IDE:PyCharm
=============================
"""
def linear_log_recur(n: int) -> int :
    if n <=1:
        return 1
    count: int = linear_log_recur(n//2) + linear_log_recur(n//2)
    for i in range(n):
        count += 1
    return count

if __name__ == '__main__':
    n: int = int(input())
    print(linear_log_recur(n))