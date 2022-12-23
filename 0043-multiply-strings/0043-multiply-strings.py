class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num3 = num1 + "*" + num2
        return str(eval(num3))
        