class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class CreateList:
    def __init__(self):
        self.head = ListNode(None)

    def InitList(self, data):
        self.head = ListNode(data[0])
        p = self.head
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            p = p.next

class Solution:
    def addTwoNumbers2(self,l1:ListNode,l2:ListNode) -> ListNode:
        re = ListNode(0)
        r = re
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            r.next = ListNode(s % 10)
            r = r.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
        if (carry > 0):
            r.next = ListNode(1)

if __name__ == '__main__':
    l1_data = [2, 4, 3]
    l2_data = [5, 6, 4]
    l1 = CreateList()
    l1.InitList(l1_data)
    l2 = CreateList()
    l2.InitList(l2_data)
    S = Solution()
    print(S.addTwoNumbers2(l1,l2))
    pass
