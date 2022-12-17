class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        top_pointer,left_pointer = 0,0
        bottom_pointer,right_pointer = len(matrix),len(matrix[0])
        ans = [[] for _ in range(right_pointer)]
        i = 0
        
        while left_pointer < right_pointer:
            for row in range(top_pointer,bottom_pointer):
                ans[i].append(matrix[row][left_pointer])
            left_pointer += 1
            i += 1
        return ans
        
                
        