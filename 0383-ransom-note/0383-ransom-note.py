class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_set = Counter(magazine)
        for ch in ransomNote:
            if magazine_set[ch] == 0:
                return False
            magazine_set[ch] -= 1
        return True

        