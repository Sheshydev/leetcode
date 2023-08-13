def bin2int(binstr):
    result = 0
    count = 0
    for i in reversed(range(len(binstr))):
        result += 2 ** count * int(binstr[i])
        count += 1
    return result

def int2bin(num):
    result = ""
    if num == 0:
        return "0"
    while num != 1 and num != 0:
        result = str(num % 2) + result
        num //= 2
    if num == 1:
        result = "1" + result
    return result

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return int2bin(bin2int(a) + bin2int(b))
    
print(int2bin(5))

