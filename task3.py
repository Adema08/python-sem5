# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def Prime_number(n):
    if n == 0 or n == 1:
        return 'not prime, not composite'
    for i in range (2, n): ##для оптимизации можно идти до скрт(н) или н/2 + 1
        if n % i == 0:
            return 'not prime'
    return 'prime'

n = int(input('Number: '))
print(Prime_number(n))