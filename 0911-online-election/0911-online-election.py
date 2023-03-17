class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.ans = []
        max_ = float("-inf")
        d = defaultdict(int)
        
        for person,time in zip(persons,times):
            d[person] += 1
            max_ = max(max_,d[person])
            if max_ == d[person]:
                self.ans.append((time, person)) 
        
    def q(self, t: int) -> int:
        
        temp = bisect.bisect_left(self.ans, (t, inf)) - 1
        return self.ans[temp][1]

  
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)