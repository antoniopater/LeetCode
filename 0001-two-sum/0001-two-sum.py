class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in dict_nums:
                return [dict_nums[diff],i]
            dict_nums[nums[i]]= i
        return []
