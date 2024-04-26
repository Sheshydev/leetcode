class Solution:
                                            def isValid(self, s: str) -> bool:
                                                parentheses = {')':'(', '}':'{', ']':'['}
                                                stack = []
                                                for c in s:
                                                    if c in parentheses.values():
                                                        stack.append(c)
                                                    else:
                                                        if stack and parentheses[c] == stack[-1]:
                                                            stack.pop()
                                                        else:
                                                            return False
                                                return False if stack else True

sol = Solution()
res = sol.isValid('[')
print(res)
