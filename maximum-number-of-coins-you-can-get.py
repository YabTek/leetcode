class Solution:
    def maxCoins(self, piles: list[int]) -> int:
      
        piles.sort()
        start = 0
        end = len(piles)-1
        num_of_coins = 0
        lst = [[] for _ in range(int(len(piles)/3))]
        i = 0
        if len(piles) == 3:
            return piles[1]
        while start < end:
            lst[i].append(piles[start])
            lst[i].append(piles[end])
            lst[i].append(piles[end-1])
            i += 1 
            start += 1
            end -= 2
        for k in range(len(lst)):
            num_of_coins += lst[k][-1]
        return num_of_coins