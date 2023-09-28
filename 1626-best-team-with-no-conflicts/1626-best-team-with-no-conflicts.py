class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = []
        dp = [0] * len(scores)
        
        for score,age in zip(scores,ages):
            players.append([age,score])
        players.sort()

        for i in range(len(scores)):
            dp[i] = players[i][1]  
            for j in range(i):
                if players[i][1] >= players[j][1]:
                    dp[i] = max(dp[i], dp[j] + players[i][1])

        return max(dp)  
        