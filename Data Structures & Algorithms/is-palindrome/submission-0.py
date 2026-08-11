class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for c in s:
            if (0 <= ord(c) - ord("a") <= 25) or (0 <= ord(c) - ord("0") <= 9):
                res += c
            elif (0 <= ord(c) - ord("A") <= 25):
                res += chr(ord(c) - ord("A") + ord("a"))
        
        if res == "".join(reversed(res)):
            return True
        return False