class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.mapping = {
            "I" : 1,
            "V" : 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        self.ten_multiples = {"I": {"V": 4, "X": 9}, "X": {"L": 40, "C": 90}, "C": {"D": 400, "M":900}}

        if len(s) == 1:
            return self.mapping[s]
        
        p1 = 0
        p2 = p1 + 1

        result = 0

        while p1 < len(s):
            c1 = s[p1]
            if p2 < len(s):
                c2 = s[p2]

                if c1 in self.ten_multiples:
                    if c2 in self.ten_multiples[c1]:
                        result += self.ten_multiples[c1][c2]
                        p1 += 1
                        p2 += 1
                    else:
                        result += self.mapping[c1]
                else:
                    result += self.mapping[c1]
            else:
                result += self.mapping[c1]
            p1 += 1
            p2 += 1
        
        return result
    
sol = Solution()
res = sol.romanToInt("CIV")
print(res)