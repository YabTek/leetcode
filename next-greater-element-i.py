class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        #result = [-1 for _ in range(len(nums1))]
        #a = [[] for _ in range(len(nums1))]
        #for i in range(len(nums1)):
         #   for j in range(len(nums2)):
           #     if nums2[j]>nums1[i] and nums2.index(nums2[j])>nums2.index(nums1[i]):
            #        a[i].append(nums2[j])

        
        #for i in range(len(a)):
          #  if len(a[i])!=0:
           #      result[i] = a[i][0]
       # return result
        answer = [-1 for _ in range(len(nums1))]
        dictionary = {}
        stk = []
        for i in nums1:
            dictionary[i] = nums1.index(i)
        for j in range(len(nums2)):
                while len(stk)>0 and  nums2[j]   > stk[len(stk)-1]:
                        temp = stk.pop()
                        answer[dictionary[temp]] =   nums2[j]  
                if nums2[j] in nums1:
                    stk.append(nums2[j])
                
        return  answer 
                       
                
              
                    
        
        