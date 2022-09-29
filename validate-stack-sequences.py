class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stk = []
        size = len(stk)
        j = 0
       #approach 1
      #  i = 0
      #  while j < len(popped):
          #  if i<len(pushed):
               # stk.append(pushed[i])
             #   size+=1
         #   if stk[-1] == popped[j]:
          #      stk.pop()
          #      size-=1
         #       i+=1
         #       j+=1
         #   else:
          #      i+=1
       # return size == 0
       
       #approach 2
        for i in range(len(popped)):
            stk.append(pushed[i])
            size +=1
            while len(stk)!=0 and stk[-1] == popped[j]:
                stk.pop()
                size-=1
                j += 1
        if size == 0:
            return True
        else:
            return False