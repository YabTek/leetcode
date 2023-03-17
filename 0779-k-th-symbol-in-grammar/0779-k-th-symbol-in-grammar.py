class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def replace(n,k):
            if n == 1:
                return 0
          
            new_num = replace(n-1, -(k//-2))
            if k % 2 == 0:
                return 1 - new_num
            else:
                return new_num
           
            
        return replace(n,k)
   
       
            
        