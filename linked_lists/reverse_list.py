# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):
        cur = None
        nxt = A
        while nxt:
            tmp = nxt.next
            nxt.next = cur
            cur = nxt
            nxt = tmp
        return cur