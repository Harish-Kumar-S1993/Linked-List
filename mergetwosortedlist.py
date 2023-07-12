# class ListNode:

#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def merge_two_sorted_list(self, l1: ListNode, l2: ListNode) -> ListNode:
        # To overcome the edge case of our output list being empty in the beginning
        dummy = ListNode()
        tail = dummy

        # condition for iterating through our lists
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            # update the tail pointer no matter which node you add
            tail = tail.next
        # what if one of our list is not empty after the above iteration?
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next


