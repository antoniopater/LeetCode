class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        m1, m2 = Counter(words1), Counter(words2)
        return sum(m1.get(w) == 1 and m2.get(w,0) == 1 for w in words1)