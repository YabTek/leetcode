class Solution:
    def sortSentence(self, s: str) -> str:
        splitted = s.split()
        arranged = [0 for _ in range(len(splitted))]     
        for word in splitted:
            for idx in word:
                try:
                    idx = int(idx)
                    arranged[idx-1] = word           
                except:
                    idx = str(idx)  
        temp = ' '.join(arranged)
        final  = ''.join([i for i in temp if not i.isdigit()])
        return final
                    
        
        