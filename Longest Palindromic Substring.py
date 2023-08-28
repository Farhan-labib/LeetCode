#Question https://leetcode.com/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(s==s[::-1]  or len(s)==1):
            return(s)

        else:
            res = [s[i: j] for i in range(len(s))
                for j in range(i + 1, len(s) + 1)]
            output=""
            for k in res:
                if(k==k[::-1]):
                    if(len(output)<=len(k)):
                        output=k
        print(output)
        return(output)