class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        # Handle the edge cases
        if not lists or len(lists) == 0:
            empty = ListNode()
            return empty

        # We have to keep merging the lists until there is only list left
        while len(lists) > 1:
            # As we merge the linked lists we are going to store them in a variable
            merged_list = []
            for i in range(0, len(lists), 2):   # Here we are going to merge poir of list. Hence, incerementer is 2
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_list.append(self.mergeSortedList(l1, l2))
            #update our list variable
            lists = merged_list

    def mergeSortedList(self, l1, l2) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
        tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next