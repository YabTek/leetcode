class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        start = 0
        end = n-1
        tokens.sort()
        score = 0
        ans_point = 0
        while start <= end:
            if power >= tokens[start]:
                score += 1
                power -= tokens[start]
                ans_point = max(ans_point,score)
                start += 1
            elif score >= 1:
                score -= 1
                power += tokens[end]
                end-=1
            else:
                return ans_point
        return ans_point