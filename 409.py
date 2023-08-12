class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = {}
        result = 0

        for c in s:
            if c in letters:
                letters[c] += 1
                if letters[c] % 2 == 0:
                    result += 2
            else:
                letters[c] = 1
        
        for c in letters:
            if letters[c] % 2 != 0:
                result += 1
                break
        
        return result

sol = Solution()
res = sol.longestPalindrome("abccccdd")
print(res)
