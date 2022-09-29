class Solution:
    def minimumBuckets(self, street: str) -> int:
        counter1=street.count('H')
        counter2=street.count('H.H')
        result = counter1-counter2
        if 'HHH' in street:
            return -1
        elif street[:2]=='HH' or street[-2:]=='HH':
            return -1
        elif street[:2]=='H':
            return -1

        return result