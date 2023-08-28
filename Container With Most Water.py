#Question https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        a=0
        k=0
        j=len(height)-1
        while k!=j:
          
                t=[]
                t.append(height[k])
                t.append(height[j])
                t1=min(t)
                t2=t1*(j-k)
                if(t2>a):
                    a=t2
                if(height[k]>height[j]):
                    j-=1
                else:
                    k+=1
        return(a)