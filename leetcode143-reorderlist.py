# class ListNode:
#
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#

class Solution:

    def reorder_list(self, head: ListNode) -> None:

        # find the middle point
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # The beginning of the second half of the list
        second = slow.next
        # end of the first list has to be set to None
        slow.next = None
        # initially previous is going to be None
        prev = None

        # Reverse the second half of the list
        while second:
            # for each iteration we are going to store our temporary variable
            tmp = second.next
            # before we shift our pointer
            second.next = prev
            # update our pointer
            prev = second
            second = tmp

        # merge the two halves
        # Remember after the reversing of second half, second will be set ot null
        # and prev will be set to last node
        first, second = head, prev
        # Remember second half is going to be small
        while second:
            # we will be storing our next links in our temporaru variables
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            #shift our pointers
            first, second = tmp1, tmp2
