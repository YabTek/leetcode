class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float("inf")
        ans = -1
        for i in range(len(points)):
            dist = math.fabs(points[i][0]-x) + math.fabs(points[i][1]-y) 
            if (dist < min_dist) and (points[i][0]==x or points[i][1]==y):
                min_dist = dist
                ans = i

        return ans       
        
        