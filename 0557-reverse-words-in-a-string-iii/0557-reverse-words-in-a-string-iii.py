class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        output = ''
        for word in words:
            output += word[::-1] + ' '
        return output.strip()
