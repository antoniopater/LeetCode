class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        sorted_s = sorted(count.items(),key=lambda x:x[1],reverse=True)
        result = "".join([char*freq for char,freq in sorted_s])
        return(result)