class Solution:
    def countArrangement(self, n: int) -> int:
        
            def backtrack(start,bit):
                nonlocal count
                if start > n:
                    count += 1
                    return 

                for i in range(1,n+1):
                    shift = 1 << i-1
                    if not (bit) & shift:
                        if i % start == 0 or start %i== 0:
                            backtrack(start+1,bit | (shift))

            count = 0
            backtrack(1,0)
            return count
