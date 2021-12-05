class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        single = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        double = {"IV":4, "IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        num = 0
        i=0
        while i < len(s):
            d = s[i]
            if i == len(s)-1:
                num += single[d]
                break
            n = s[i:i+2]
            if n in double:
                num += double[n]
                i = i +2
                continue
            else:
                num += single[d]
                i += 1
        return num
