#Question https://leetcode.com/problems/two-sum/



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=len(nums)-1
        j=len(nums)-2
        li=[1]

        while sum(li)!=target:
            if(nums[i]+nums[j]==target):
                li=[]
                li.append(i)
                li.append(j)
                return li
                break
            elif(j==0):
                i-=1
                j=i-1
            else:
                j-=1

