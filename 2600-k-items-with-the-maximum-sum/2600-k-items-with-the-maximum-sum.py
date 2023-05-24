class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        if k < numOnes:
            return k
        
        if numOnes >= k:
            return numOnes
       
        elif numOnes + numZeros >= k:
            return numOnes
        else:
            return numOnes - (k - numZeros - numOnes)
        