class Solution:
    def numberToWords(self, num: int) -> str:
      
        under20 = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine","Ten", "Eleven", "Twelve", "Thirteen", "Fourteen","Fifteen", "Sixteen", "Seventeen", "Eighteen",  "Nineteen"]
        under100 = ["Twenty", "Thirty", "Forty", "Fifty","Sixty", "Seventy", "Eighty", "Ninety"]
        larger = [100, 1000, 1000*1000, 1000*1000*1000]
        chunks = ["Hundred", "Thousand", "Million", "Billion"]
        if num == 0:
              return "Zero"
        def toword(num):
            if int(num)==0:
                return ''
            elif num < 20:
                return ' ' + under20[int(num-1)]
            elif num<100:    
                return ' ' + under100[int(num/10 - 2)] + toword(num % 10) 
            i=3
            while i>=0:
                if num >= larger[i]:
                    return toword(num/larger[i]) + " " + chunks [i] + toword(num % larger [i])
                i+=1
            return ""                
        ans = toword(num)
        ans = ans[1:len(ans)]
       
        return ans
        