class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(s)
        i = 0
        ans = []
        for j in spaces:
            ans.append(s[i:j])
            i = j
        ans.append(s[spaces[-1]:n])
        return " ".join(ans)