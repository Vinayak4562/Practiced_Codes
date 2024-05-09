class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(ListNode):
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2           
        return dummy.next
    
list1 =[1,2,3,7,8,9]
list2 = [4,5,6,9,10]
L = Solution()
A =L.mergeTwoLists(list1, list2)
print(A)