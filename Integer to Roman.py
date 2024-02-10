https://leetcode.com/problems/integer-to-roman/description/


class Solution:
    def intToRoman(self,num: int) -> str:
        intRom={"I":1,
                "IV":4,
                "V":5,
                "IX":9,
                "X":10,
                "XL":40,
                "L":50,
                "XC":90,
                "C":100,
                "CD":400,
                "D":500,
                "CM":900,
                "M":1000}
        res=""
        for k,v in reversed(intRom.items()):
            while num>0:
                if v<=num:
                    res+=k
                    num-=v
                else:
                    break
        return res


