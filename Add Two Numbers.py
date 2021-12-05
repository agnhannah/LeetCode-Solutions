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
        num1 = ""
        num2 = ""
        node1 = l1
        node2 = l2
        while node1 or node2:
            if node1:
                num1 = str(node1.val) + num1
                node1 = node1.next
            if node2:
                num2 = str(node2.val) + num2
                node2 = node2.next
        ans = str(int(num1)+int(num2))
        a1 = ListNode(int(ans[-1]))
        b1 = a1
        for i in ans[:-1][::-1]:
            a2 = ListNode(int(i))
            b1.next = a2
            b1 = a2
        return a1
