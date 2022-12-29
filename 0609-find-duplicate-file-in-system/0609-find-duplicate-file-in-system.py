class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans = []
        hash_map = defaultdict(list)
        i = 0
        n = len(paths)
        
        while i < n:
            directory = paths[i].split()
            for j in range(1,len(directory)):
                text_file = directory[j].split("(")
                hash_map[text_file[1]].append((directory[0],text_file[0]))
            i += 1
            
        for content,items in hash_map.items():
            if len(items) >= 2:
                temp = []
                for route,text_file in items:
                    temp.append(route + '/' + text_file)
                ans.append(temp)
                
        return ans
                    
                
        