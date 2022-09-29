class Solution:
    def isPowerOfThree(self, n: int) -> bool:
         if (n <= 0):
            return False
         while n > 1:
            if n % 3 !=0:
               return False
            n = n//3
         return True
      

# import math
# def j():
#     n = 81

#     for i in range(1,n):

#        if int(math.pow(3,i)) == n:
      
#           return True
#        elif int(math.pow(3,i)) !=n:
#           return False
# print(j())