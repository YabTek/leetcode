class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ball_left = 0
        ball_right = 0
        ans = [0] * len(boxes)
        left_tot = 0
        right_tot = 0
        
        for i in range(1,len(boxes)):
            if boxes[i-1] == '1': 
                ball_left += 1
            left_tot += ball_left
            ans[i] = left_tot
        for j in range(len(boxes)-2, -1, -1):
            if boxes[j+1] == '1': 
                ball_right += 1
            right_tot += ball_right
            ans[j] += right_tot
            
        return ans

            
            