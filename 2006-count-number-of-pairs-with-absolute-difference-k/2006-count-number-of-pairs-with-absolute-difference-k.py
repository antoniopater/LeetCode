class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq, counter = {},0
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        for num in nums:
            if num + k in freq:
                counter += freq[num+k]
        return counter 
            