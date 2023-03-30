class Solution:
    def findComplement(self, num: int) -> int:
        binary = ""
        ans = ""
        
        while num > 0:
            binary += str(num%2)
            num = num >> 1
            
        for num in binary[::-1]:
            if num == '0':
                ans += '1'
            else:
                ans += '0'
                
        return int(ans,2)
            
            
        