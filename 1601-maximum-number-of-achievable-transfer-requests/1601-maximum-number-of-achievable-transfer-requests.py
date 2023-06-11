class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def backtrack(i):
            
            nonlocal ans, temp

            if all(count[key] == 0 for key in count):
                ans= max(ans, temp)

            if i >= len(requests):
                return                         

            for i in range(i, len(requests)):
                from_, to = requests[i]

                temp += 1
                count[from_] -= 1
                count[to] += 1
                
                backtrack(i + 1)

                temp -= 1
                count[from_] += 1
                count[to] -= 1

        count = defaultdict(int) 
        ans = 0
        temp = 0
        backtrack(0)
        
        return ans
        
       