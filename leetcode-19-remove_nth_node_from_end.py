class Listnode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEndList(self, head: Listnode, n: int) -> Listnode:
        dummy = Listnode(0, head)   # initialize dummy and make it point to the head
        left = dummy    # initialize left pointer to dummy
        right = head    # initialize right pointer to head

        # we need right pointer to be at head + n, so we need a loop to do this
        while n > 0 and right:
            right = right.next
            n -= 1  # Once n = 0 we have shifted the right to the amount we want ot shift

        # start shifiting the pointers
        while right:
            left = left.next
            right = right.next

        # delete the nth node
        left.next = left.next.next

        return dummy.next
