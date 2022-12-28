class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(2)] 
        winners = []
        losers = []
        
        for players in matches:
            winners.append(players[0])
            losers.append(players[1])
            
        count = Counter(losers)    
        for player,cnt in count.items():
            if cnt == 1:
                ans[1].append(player)
        

        only_winners = set(winners)-set(losers)
        for player in only_winners:
            ans[0].append(player)
            
        ans[0].sort()
        ans[1].sort()
        
        return ans
            
        