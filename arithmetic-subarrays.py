class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        store = []

        for a,b in zip(l,r):
            store.append(nums[a:b+1])
        answer = [True for _ in range(len(store))]
        
        for i in range(len(store)):
            store[i].sort()
            difference = store[i][1]-store[i][0]
            print(store[i])
            print(difference)

            for j in range(len(store[i])-1):
                if store[i][j+1]-store[i][j] != difference:
                    answer[i] = False
                               
        return answer