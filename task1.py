# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an
# , ..., где a0= 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

def fib(n):
    if n in [0, 1]:
        return 1
    return fib(n - 1) + fib(n - 2)

n = int(input('Order of number: '))
for i in range(0, n):
    print(fib(i), end=' ')