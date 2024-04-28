import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[\W_]', '', s).lower()

        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1+=1
            p2-=1
        return True
    

sol = Solution()
print(sol.isPalindrome("LMAO"))