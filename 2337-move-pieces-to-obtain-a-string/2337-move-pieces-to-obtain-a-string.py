class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start = [(char, i) for i, char in enumerate(start) if char != '_']
        target = [(char, i) for i, char in enumerate(target) if char != '_']
        
        if len(start) != len(target):
            return False
        
        for (ch1, i), (ch2, j) in zip(start, target):
            if ch1 != ch2:
                return False
            if ch1 == 'L' and i < j:  
                return False
            if ch1 == 'R' and i > j:  
                return False

        return True 