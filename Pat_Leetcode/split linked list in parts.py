class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l=[]
        t=head
        c=0
        while t:
            t=t.next
            c+=1
        q,r=divmod(c,k)
        print(q,r)
        t=head
        for i in range(k):
            a=b=ListNode(0)
            for j in range(q+(i<r)):
                if t:
                    b.next=b=ListNode(t.val)
                    t=t.next
            l.append(a.next)
        return l