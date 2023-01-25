class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left = 0
        right = len(skill) - 1
        chemistry = 0
        total = skill[left] + skill[right]
        
        while left < right:
            if skill[left] + skill[right] != total:
                return -1
            chemistry += skill[left] * skill[right]
            left += 1
            right -= 1
            
        return  chemistry
            
            
            
        