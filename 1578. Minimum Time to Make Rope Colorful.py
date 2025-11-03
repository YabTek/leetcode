class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        j = 0
        
        for i in range(1, len(colors)):
            if colors[i] == colors[j]:
                if neededTime[i] <= neededTime[j]:
                    ans += neededTime[i]
                else:
                    ans += neededTime[j]
                    j = i
            else:
                j = i

        return ans


