class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
      #  points=[]
       # for i in range(len(questions)):
         #   start = questions[i]
           # temp = 0
            #if i+1+questions[i][1] == len(questions):
            #    idx = i+1+questions [i][1]
             #   end = questions[idx]
               # points.append(start[0]+end[0])
         #   elif i+1+questions[i][1] < len(questions):

         #       idx = i+1+questions [i][1]
                #idx2=1+i+questions [idx][1]
                

           #     end = questions[idx:idx2]
           #     for lst in end:
             #       temp+=lst[0]
                #points.append(start[0]+temp)    

         #   else:
                #points.append(start[0])
          # print(points)

       # return max(points)
      
        ans = 0
        start = len(questions)-1
        points = [0 for _ in range(len(questions)+1)]

        while start >= 0:
            
              
            if start+1+questions[start][1] == len(questions):
                idx = start+1+questions[start][1]
                end = questions[start][0] +points[idx]
                points[start] = max(end,points[start+1])

            
            elif start+1+questions[start][1] < len(questions):
                idx = start+1+questions[start][1]

                end = questions[start][0] + points[idx]
                points[start] = max(end,points[start+1])
        

            else:

                end = questions[start][0] 
                points[start] = max(end,points[start+1])
            start-=1
        ans = points[0]



        return ans