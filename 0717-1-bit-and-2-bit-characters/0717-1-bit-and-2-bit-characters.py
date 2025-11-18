class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        flag = 0
        bits = bits[::-1]
        while bits:
            flag = bits.pop()
            if flag:
                bits.pop()
        return not flag