class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # t=head
        # l=[]
        # while t:
        #     p=t
        #     a=p.val
        #     k=a
        #     p=p.next
        #     while p:
        #         if p.val>a:
        #             a=p.val
        #             break
        #         p=p.next
        #     if k==a:
        #         l.append(0)
        #     else:
        #         l.append(a)
        #     t=t.next
        # return l
        p=-1
        s,a=[],[]
        while head:
            p+=1
            a.append(0)
            while s and s[-1][1]<head.val:
                index,value=s.pop()
                a[index]=head.val
            s.append((p,head.val))
            head=head.next
        return a