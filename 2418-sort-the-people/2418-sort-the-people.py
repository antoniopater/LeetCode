class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_to_name_map = dict(zip(heights,names))
        sorted_hights = sorted(heights,reverse=True)
        return [height_to_name_map[h] for h in sorted_hights]