# source: https://leetcode.com/problems/merge-two-sorted-lists/?envType=featured-list&envId=top-interview-questions

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100

# Pseudocode:
# 1. Create a new linked list
# 2. Iterate over the two lists
# 3. Compare the values of the two lists
# 4. Add the smaller value to the new list

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create a new linked list
        new_list = ListNode()
        # create a pointer to the new list
        new_list_pointer = new_list
        # create a pointer to the first list
        l1_pointer = l1
        # create a pointer to the second list
        l2_pointer = l2
        # iterate over the two lists
        while l1_pointer and l2_pointer:
            # compare the values of the two lists
            if l1_pointer.val < l2_pointer.val:
                # add the smaller value to the new list
                new_list_pointer.next = l1_pointer
                # move the pointer of the first list
                l1_pointer = l1_pointer.next
            else:
                # add the smaller value to the new list
                new_list_pointer.next = l2_pointer
                # move the pointer of the second list
                l2_pointer = l2_pointer.next
            # move the pointer of the new list
            new_list_pointer = new_list_pointer.next
        # if there are still nodes in the first list
        while l1_pointer:
            # add the remaining nodes to the new list
            new_list_pointer.next = l1_pointer
            # move the pointer of the first list
            l1_pointer = l1_pointer.next
            # move the pointer of the new list
            new_list_pointer = new_list_pointer.next
        # if there are still nodes in the second list
        while l2_pointer:
            # add the remaining nodes to the new list
            new_list_pointer.next = l2_pointer
            # move the pointer of the second list
            l2_pointer = l2_pointer.next
            # move the pointer of the new list
            new_list_pointer = new_list_pointer.next
        # return the head of the new list
        return new_list.next

l1 = [1,2,4]
l2 = [1,3,4]

l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

print(Solution().mergeTwoLists(l1, l2))