class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = 0
        cnt = Counter(stones)
        jewels_set = set(jewels)
        for j, freq in cnt.items():
            if j in jewels_set:
                counter += freq
        return counter 