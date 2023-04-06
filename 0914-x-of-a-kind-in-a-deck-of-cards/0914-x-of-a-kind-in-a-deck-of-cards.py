class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1:
            return False
        
        def find_gcd(a,b):
            if b == 0:
                return a
            else:
                return find_gcd(b,a%b)
            
        count = Counter(deck)
        cur = count[deck[0]]
        
        gcd = find_gcd(count[deck[0]],count[deck[1]])
        
        for num,cnt in count.items():
            if num != deck[0] and num != deck[1]:
                gcd = find_gcd(gcd,cnt)
                
        if gcd != 1:
            return True
        else:
            return False
                
        