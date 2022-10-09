class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+1)
        
        for b in bookings:
            ans[b[0]-1]+=b[2]
            ans[b[1]]-=b[2]
        
        
        for i in range(1,n):
            ans[i]+=ans[i-1]   
        del ans[-1]
        
        return ans

        