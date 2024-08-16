class Solution(object):
    def middleNode(self, head):
        if head is None:
            return None
        count = 0
        curr = head
        while curr is not None:
            curr = curr.next
            count += 1
        mid = head
        for _ in range(count/2):
            mid = mid.next
        return mid