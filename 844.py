class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return self.getActualStr(s) == self.getActualStr(t)

    def getActualStr(self, txt):
        arr = []
        for i in range(len(txt)):
            if txt[i] == '#':
                if i != 0:
                    arr = arr[:-1]
            else:
                arr.append(txt[i])
        return ' '.join(arr)

sol = Solution()
res = sol.backspaceCompare("asb#c", "ad#c")
print(res)