class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i = 0
        j = 0
        ans = 0
        trainers.sort()
        players.sort()
       
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                ans += 1
                i += 1
            j += 1
            
        return ans 
        