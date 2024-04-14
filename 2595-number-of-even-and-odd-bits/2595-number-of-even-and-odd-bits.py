class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        n = list(bin(n))[2:][::-1]
        even = 0
        odd = 0
        
        for i in range(len(n)):
            if n[i] == '1':
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
                    
        return [even, odd]
            
        
        
        
        