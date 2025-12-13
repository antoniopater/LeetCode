class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0, len(height) -1
        max_sq = 0
        while l<r:
            sq = abs(l-r) * min(height[l], height[r])

            if sq > max_sq:
                max_sq = sq
            if height[l]<height[r]:
                l +=1
            else:
                r-=1
        return max_sq