class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        #approach1 2list
       # lst1=[]
       # lst2=[]
      #  for a in nums:
        #    if a != 0:
        #        lst1.append(a)
         #   else:
        #        lst2.append(a)
      #  result = lst1+lst2
      #  return result
        #approach2 2pointers
        size = len(nums)-1
        end = 0
       
        for start in range(size+1):
            if nums[start]!=0:
                (nums[start],nums[end])=(nums[end],nums[start])
                end+=1