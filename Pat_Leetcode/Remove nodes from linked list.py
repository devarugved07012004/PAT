class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        t=head
        while t:
            while l and l[-1]<t.val:
                l.pop()
            l.append(t.val)
            t=t.next
        a=ListNode(0)
        b=a
        for i in l:
            b.next=ListNode(i)
            b=b.next
        return a.next