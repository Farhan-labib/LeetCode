#Question https://leetcode.com/problems/median-of-two-sorted-arrays/



class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        temp3=nums1+nums2
        for i in range(n-1):
            for j in range(n-i-1):
                if(temp3[j] > temp3[j+1]):
                    temp3[j], temp3[j+1] = temp3[j+1], temp3[j]


                    

        print(temp3)
        if(len(temp3)%2==0):
            t1=temp3[(len(temp3)/2)-1]
            t2=temp3[len(temp3)/2]
            return float(t1+t2)/2
        else:
            return (temp3[((len(temp3))//2)])

