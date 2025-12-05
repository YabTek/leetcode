class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            enc_word = str(len(word)) + "|" + word
            encoded.append(enc_word)

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        i = 0
        j = 0
        ans = []

        while i < len(s):
            if s[i] == "|":
                word_len = int(s[j:i])
                i += 1
                ans.append(s[i:i+word_len])
                i += word_len
                j = i
            else:
                i += 1
            

        return ans

