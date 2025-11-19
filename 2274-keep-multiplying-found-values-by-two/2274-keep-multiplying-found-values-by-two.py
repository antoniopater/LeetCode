class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        if original in nums:
            i = original
            while i in nums:
                i = i*2
            return i
        return original