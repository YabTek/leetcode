class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = 0
        dictionary = {}
        ans = []
        num_of_char = 0

        for idx,char in enumerate(s):
            dictionary[char] = idx
        for idx,char in enumerate(s):
            num_of_char += 1
            last_seen = max(last_seen,dictionary[char])
            if idx == last_seen:
                ans.append(num_of_char)
                num_of_char = 0
               
        return ans