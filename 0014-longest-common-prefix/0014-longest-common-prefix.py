class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans  = ""
        shortest = min(strs , key = len)
        if len(shortest) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        for chars in zip(*strs):
            unique_chars = set(chars)
            if len(unique_chars) == 1:
                ans += chars[0]
            else:
                return ans
        return ans

        