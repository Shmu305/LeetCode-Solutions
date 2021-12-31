class Solution(object):
    def reorderList(self, head):
        #find the middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev  = None
        #reverse second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        #combine
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2
        
