class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash_map = defaultdict(int)
        ans = []
        for domains in cpdomains:
            count,dom = domains.split()
            domain = dom.split('.')
            for i in range(len(domain)):
                temp = '.'.join(domain[i:])
                hash_map[temp] += int(count)
                
        for domain,count in hash_map.items():
            ans.append(str(count) + ' ' + domain)
            
        return ans