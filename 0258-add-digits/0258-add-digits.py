class Solution:
    def addDigits(self, num: int) -> int:
        
        def sum(num):
            if num <= 9:
                return num
            num = (num%10) + sum(num//10)
            return (num%10) + sum(num//10)
       
        return sum(num)
