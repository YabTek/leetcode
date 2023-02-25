class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for char in s:
            if char != '*':
                stk.append(char)
            else:
                stk.pop()
        return "".join(stk)