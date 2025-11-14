class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        i = 0
        j = len(skill) - 1
        skill.sort()
        prev_tot = skill[i] + skill[j]
        ans = 0

        while i < j:
            left = skill[i]
            right = skill[j]
            tot = left + right

            if tot != prev_tot:
                return -1
            ans += left * right

            i += 1
            j -= 1

        return ans





        