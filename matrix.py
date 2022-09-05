class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
       
        m = len(matrix)-1
        n = len(matrix[0])-1
        answer = []
        top_pointer,left_pointer = 0,0
        bottom_pointer = m
        right_pointer = n

        while top_pointer <= bottom_pointer and left_pointer<=right_pointer:
            for column in range(left_pointer, right_pointer + 1):

                  answer.append(matrix[top_pointer][column])

            for row in range(top_pointer + 1, bottom_pointer):

                answer.append(matrix[row][right_pointer])

            for column in range(right_pointer,left_pointer-1,-1):

                if top_pointer < bottom_pointer:

                    answer.append(matrix[bottom_pointer][column])

            for row in range(bottom_pointer-1,top_pointer,-1):

                if left_pointer < right_pointer:

                    answer.append(matrix[row][left_pointer])

            left_pointer+=1                 
            right_pointer-=1
            top_pointer+=1
            bottom_pointer-=1

            

        return answer