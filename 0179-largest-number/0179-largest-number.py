class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums_sorted = sorted(nums, key=lambda n: n*10,reverse=True)
        if nums_sorted[0] == "0":
            return "0"
        return "".join(nums_sorted)
        
        
        
        