class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # a=0
        # b=ListNode(0)
        # t=b
        # while head:
        #     if head.val==0:
        #         t.next=ListNode(a)
        #         t=t.next
        #         a=0
        #     else:
        #         a+=head.val
        #     head=head.next
        # return b.next.next
        a=ListNode(0)
        a.next=head
        c=a
        while c.next:
            p=c
            if c.next.val==0:
                c=c.next
            if c.next:
                c.val+=c.next.val
                c.next=c.next.next
        p.next=None
        return head