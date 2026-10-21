class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        def helper(l, r):
            nonlocal res
            # nonlocal resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            # odd length palindrome
            l, r = i, i
            helper(l, r)

            # even length palindromes
            l, r = i, i + 1
            helper(l, r)


        return res