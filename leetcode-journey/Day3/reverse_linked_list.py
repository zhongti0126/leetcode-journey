class Solution(object):
def reverseList(self, head):
  
  prev = None
  current = head
  
  while current:
    
    newNode = current.next
    
    current.next = prev
    
    prev = current
    
    current = newNode
    
  return prev 
