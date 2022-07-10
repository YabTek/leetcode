from re import A


A = [3,1,3,4,3]
A.sort()
l =[]
k = 6
y = set()
operation = 0
i = 0
j = len(A) -1 
while (i < j):
    if A[i] + A[j] == k:
           print(A[i])
           A.remove(A[i])
           A.remove(A[j])
    i +=1
    j -=1   

# for i in range(len(n)):
#     for j in range(i,len(n)):
#          if i == j:
#              continue
        
#          else:
#             if n[i]+n[j] == k: 
                       
#                 operation+=1
#                 n.remove(n[i])
#                 n.remove(n[j])
                
               

        
# print(y)               
print(A)
print(operation)