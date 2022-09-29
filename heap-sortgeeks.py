#User function Template for python3
class Solution:
    
    def heapify(self,arr, n, i):
        if i < n and 2*i+1<n and 2*i+2<n:
            parent = arr[i]
            left_child = arr[2*i+1]
            right_child = arr[2*i+2]
        
            greater = max(parent,left_child,right_child)
            if greater != parent:
                (parent,greater) = (greater,parent)
                Solution.heapify(self,arr,n,arr.index(greater))     
  
    def buildHeap(self,arr,n):
        i = n//2-1
        while i >= 0:
            Solution.heapify(self,arr,n,i)
            i-=1
        Solution.HeapSort(self,arr,n)
        
  
    def HeapSort(self, arr, n):

        #Solution.buildHeap(self,arr,n)
        i = n-1
        while i >= 0:
            (arr[0],arr[i]) = (arr[i],arr[0])
            Solution.heapify(self,arr,i,0)
            i -=1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).next
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.stdout.write(_OUTPUT_BUFFER.getvalue())

if name == 'main':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code End
# } Driver Code