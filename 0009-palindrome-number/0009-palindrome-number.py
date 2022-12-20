class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse = 0
        y = x
        if y < 0:
            return False
        while y:
            reverse = reverse * 10 + y % 10
            y //= 10

        return x == reverse
      
       