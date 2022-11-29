# sum 2 linked lists backwards

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2, c = 0):
        sum_l = None
        cur1 = l1
        cur2 = l2
        remind = 0
        cur = sum_l
        
        while(cur1 and cur2):
            
            cur = ListNode((cur1.val + cur2.val + remind) % 10)
            
            if (sum_l == None):
                sum_l = cur
            else:
                temp = sum_l
                while (temp.next):
                    temp = temp.next
                temp.next = cur
            
            if (cur1.val + cur2.val <= 9):
                remind = 0
            else:
                remind = 1
                
            cur1 = cur1.next
            cur2 = cur2.next
        
        if(remind == 1):
            temp = sum_l
            while (temp.next):
                temp = temp.next
            temp.next = ListNode(remind)
        
        return sum_l
    
    
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(7)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(9)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val,)
    result = result.next
# 7 0 8