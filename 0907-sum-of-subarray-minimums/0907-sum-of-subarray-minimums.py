class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:   
        stk = []
        ans = 0
        arr.append(0)
        arr = [0] + arr
       
        for i in range(len(arr)):
            while stk and  arr[i] < arr[stk[-1]]:
                prev_smaller = stk[-2]
                cur_num = stk.pop()
                next_smaller = i
                length = (cur_num-prev_smaller)*(next_smaller-cur_num)
                ans += ((length)*(arr[cur_num]))
                
            stk.append(i)
                  
        return (ans) % (10**9+7)
