class Solution:
    def maxFreqSum(self, s: str) -> int:
        samogloski = {'a':0,'o':0,'e':0,'i':0,'u':0}
        freq = {}
        for x in range(len(s)):
            if s[x] in samogloski.keys():
                samogloski[s[x]] = samogloski.get(s[x],0) + 1
            else:
                freq[s[x]] = freq.get(s[x],0) + 1
        max_samogloski = max(samogloski.values())
        max_freq = max(freq.values()) if freq else 0 
        return max_samogloski + max_freq