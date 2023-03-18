class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for n in digits:
            num += str(n)
        num =  int(num)
        num += 1
        ans = []
        for n in str(num):
            ans.append(int(n))
            
        return ans
        