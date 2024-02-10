https://leetcode.com/problems/roman-to-integer/description/


class Solution:
    def romanToInt(self, s: str) -> int:
        d1={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900,'I':1,
        'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        summ=0
        i=0
        j=1
        while(i<=len(s)-1):
            t=""
            if(j<len(s)):
                t=s[i]+s[j]
            if(t in d1):
                summ+=d1.get(t)
                i+=2
                j+=2
            else:
                summ+=d1.get(s[i])
                i+=1
                j+=1
        return(summ)
        


        
