class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        ans = 0
        boxTypes.sort(key=lambda x: -x[1])

        for a,b in boxTypes:
            if a < truckSize:
                ans += a*b
                truckSize -= a
            else:
                ans += truckSize*b
                break

        return ans
        