class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(s) != len(words):
            return False
        output = ""
        for i in words:
            output += i[0]
        if output == s:
            return True
        return False