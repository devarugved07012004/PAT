class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a=b=head
        l=[]
        while b:
            l.append(a.val)
            a=a.next
            b=b.next.next
        k=0
        while a:
            k=max(l.pop()+a.val,k)
            a=a.next
        return k