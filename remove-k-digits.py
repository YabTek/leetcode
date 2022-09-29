class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        size = len(num)
        stk = []
        i = 0
        while i < size:
            while len(stk) > 0 and k != 0 and stk[-1] > num[i]:
                    stk.pop()
                    k -= 1
            stk.append(num[i])
            i += 1

        return "".join(stk).lstrip('0')[:-k or None] or '0'