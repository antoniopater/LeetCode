class Solution:
    def frequencySort(self, s: str) -> str:
        count = defaultdict(int)
        for ch in s:
            count[ch]+=1
        chars_sorted = sorted(count, key=count.get, reverse=True)
        return "".join(ch*count[ch] for ch in chars_sorted)