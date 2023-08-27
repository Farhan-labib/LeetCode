#Question https://leetcode.com/problems/longest-substring-without-repeating-characters/



class Solution(object):
    def lengthOfLongestSubstring(self, s):
        a=[]
        t=""
        if(s==""):
            return 0
        if(s==" "):
            return 1
        if(len(s)==1):
            return 1
        while (len(s)!=1):
            for j in s:
                if(j not in t):
                   t+=j
                else:
                   a.append(t)
                   t=""
                   s=s[1::]
                   break
            a.append(t)
        m=-1
        print(a)
        for j in a:
            if(len(j)>m):
                m=len(j)
        return m