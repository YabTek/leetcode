class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = ""
        
        while n > 0:
            binary += str(n%2)
            n //= 2
            
        for i in range(1,len(binary[::-1])):
            if binary[i] == binary[i-1]:
                return False
        return True
            
            
        