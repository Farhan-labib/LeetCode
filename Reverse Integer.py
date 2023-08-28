#Question https://leetcode.com/problems/reverse-integer/


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x=str(x)
        t=""
        if(x[0]=="-"):
            x=x[1::]
            t="-"
        c=len(x)-1
        s=''
        while c!=0:
            if(x[c]!=0):
                s+=x[c]
            c-=1
        s+=x[0]
        temp=t+s
        temp=int(temp)
        print(temp)
        if(temp>-2**31 and temp<2**(31)-1):
             return int(temp)
        else:
            return 0
