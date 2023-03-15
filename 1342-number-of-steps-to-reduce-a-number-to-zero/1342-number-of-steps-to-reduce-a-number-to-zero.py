class Solution:
    def numberOfSteps(self, num: int) -> int:
        def reduce(num,steps):
            if num == 0:
                return steps
            if num % 2 == 0:
                return reduce(num//2,steps+1)
            
            return reduce((num-1),steps+1)
        
        return reduce(num,0)
        