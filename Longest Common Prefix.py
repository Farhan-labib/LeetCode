https://leetcode.com/problems/longest-common-prefix/description/


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=min(strs,key=len)
        i=0
        s=""
        t=""
        for j in l:
            t=""
            for k in strs:
                if(j==k[i]):
                    t+=j
                else:
                    break
            i+=1
            if(len(t)==len(strs)):
               s+=t[0]
            else:
                break
        
        return(s)



