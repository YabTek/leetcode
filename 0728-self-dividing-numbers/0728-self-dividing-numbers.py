class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        
        for num in range(left,right+1):
            flag = True
            for div in str(num):
                div = int(div)
                if div == 0:
                    flag = False
                    continue
                if num % div != 0:
                    flag = False
            if flag:
                ans.append(num)
                
        return ans
                
        