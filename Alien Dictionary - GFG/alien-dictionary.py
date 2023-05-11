#User function Template for python3
from collections import defaultdict, deque

class Solution:
    def findOrder(self,alien_dict, N, K):
        
        graph = defaultdict(list)
        in_coming = defaultdict(int)
        order = []
        starting_alphabets = []
        n = len(alien_dict)
        queue = deque()
        
        for i in range(n-1):
            for char1,char2 in zip(alien_dict[i],alien_dict[i+1]):
                
                if char1 == char2:
                    continue
               
                graph[char1].append(char2)
                in_coming[char2] += 1
                break
            starting_alphabets.append(alien_dict[i])

        starting_alphabets.append(alien_dict[n-1])
        starting_alphabets = set(list("".join(starting_alphabets)))

        for chars in starting_alphabets:
            if in_coming[chars] == 0:
                queue.append(chars)
        
        def bfs(queue):
       
            while queue:
                    char = queue.popleft()
                    order.append(char)
                    
                    for neighbour in graph[char]:
                        in_coming[neighbour] -= 1
                        
                        if in_coming[neighbour] == 0:
                            queue.append(neighbour)
                            
            return order
            
        return bfs(queue)
        
        
                    
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends