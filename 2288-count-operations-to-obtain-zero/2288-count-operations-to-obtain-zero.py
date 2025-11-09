def sub_two_numbers(a, b):
    if a >= b:
        return a - b, b
    else:
        return a, b - a

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        counter = 0
        a, b = num1, num2
        while a > 0 and b > 0:
            a, b = sub_two_numbers(a, b)
            counter += 1
        return counter
