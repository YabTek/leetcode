class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ds1 = defaultdict(int)
        ds2 = defaultdict(int)
        
        if len(s1) > len(s2):
            return False
        
        for char in s1:
            ds1[char] += 1
        for i in range(len(s1)):
            ds2[s2[i]] += 1
        if ds1 == ds2:
            return True
        
        j = 0
        for i in range(len(s1),len(s2)):
            ds2[s2[i]] += 1
            ds2[s2[j]] -= 1
            if ds2[s2[j]] == 0:
                del ds2[s2[j]]
            j += 1 
            if ds1 == ds2:
                return True
            
        return False
            