class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mem = [0] * (ord('z') - ord('a') + 1) 

        for i in range(len(s)):
            mem[ord(s[i]) - 97] += 1
            mem[ord(t[i]) - 97] -= 1

        for i in range(len(mem)):
            if mem[i] != 0:
                return False
            
        return True
    
res = Solution().isAnagram("anagram", "aagaarnm")
print(res)