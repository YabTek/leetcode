class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        queen = set()
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1], 
                  [-1, -1],  [-1, 1], [1, -1], [1, 1]]
        
        for lst in queens:
            temp = tuple(lst)
            queen.add(temp)
                   
        for x, y in directions:
            a, b = king
            while 0 <= a < 8 and 0 <= b < 8:
                a += x
                b += y
                if (a, b) in queen:
                    ans.append((a, b))
                    break
        return ans
        