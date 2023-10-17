from itertools import combinations


class Solution:
    def countVowels(self, word: str) -> int:
        vowels = ['a','e','i','o','u']
       
        
      #  counter = 0
      #  substring = [word[a:b] for a, b in combinations(range(len(word) + 1), r=2)]
     
      #  joined = "".join(substring)
     
    
      #  for letter in joined:
        #    if letter in vowels:
        #        counter += 1
      #  return counter
        
        counter = 0
        n = len(word)
        idx = 0
        while idx < n:
            if word[idx] in vowels:

                temp = (idx+1)*(n-idx)

                counter += temp
            
            idx+=1
            
        return counter    
            

               
     
                    
       

        
        