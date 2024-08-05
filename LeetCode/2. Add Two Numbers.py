# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Optional():
    def __init__(self) -> None:
        self.l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))  #ListNode(2,ListNode(4,ListNode(3))) #ListNode(0) 
        
        self.l2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9)))) # ListNode(5,ListNode(6,ListNode(4))) #ListNode(0) 
        
    #   [ListNode(9,9),ListNode(9,9),ListNode(9,9),ListNode(9)]]

class Solution:
    def addTwoNumbers(self, l1: list[ListNode], l2: list[ListNode]) -> list[int]:

        val_l1,val_l2 = list(),list()
        while True:
            val_l1.append(l1.val)
            if l1.next == None:
                break
            l1 = l1.next
        while True:
            val_l2.append(l2.val)
            if l2.next == None:
                break
            l2 = l2.next

        sum_l1 = (sum([x * int(f"1{'0'*i}") for i,x in enumerate(val_l1)]))
        sum_l2 = (sum([x * int(f"1{'0'*i}") for i,x in enumerate(val_l2)]))
        sum_all = str(sum_l1 + sum_l2)

        size_sum_all = len(sum_all)-1
        new_list_node = ListNode(int(sum_all[size_sum_all]))
        aux = new_list_node
        while True:
            if size_sum_all <= 0:
                break
            aux.next = ListNode(int(sum_all[size_sum_all-1]))
            aux = aux.next 
            size_sum_all -= 1
            
        return [new_list_node]


o = Optional()
s = Solution()
print(s.addTwoNumbers(o.l1,o.l2))