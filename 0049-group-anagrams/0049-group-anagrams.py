class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lists = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            lists[key].append(s)
        return list(lists.values())