#Question https://leetcode.com/problems/add-two-numbers/



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t1=l1
        t2=l2
        s1=""
        s2=""
        while t1!=None:
            s1+=str(t1.val)
            t1=t1.next
        while t2!=None:
            s2+=str(t2.val)
            t2=t2.next 
        s1=s1[::-1]
        s2=s2[::-1]
        s3=int(s1)+int(s2)
        head=ListNode(s3%10,None)
        temp=head
        s3=s3//10
        while s3!=0:
            n=ListNode(s3%10,None)
            temp.next=n
            temp=temp.next
            s3=s3//10
        return head

        

