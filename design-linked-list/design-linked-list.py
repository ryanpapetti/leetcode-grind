class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.linked_list = None
        
    
    def __repr__(self):
        vals = []
        cursor = self.linked_list
        while cursor:
            vals.append(str(cursor.val))
            cursor = cursor.next
        final_str = '->'.join(vals)
        return final_str
        

    def get(self, index: int) -> int:
        if not self.linked_list:
            return -1
        
        
        cursor = self.linked_list
        for _ in range(index): 
            try:
                cursor = cursor.next
            except:
                return -1
        
        if cursor:
            return cursor.val
        return -1
            
        
        

    def addAtHead(self, val: int) -> None:
        new_node = Node(val,self.linked_list)
        self.linked_list = new_node
        
        

    def addAtTail(self, val: int) -> None:
        new_node = Node(val,None)
        if self.get(0) == -1:
            self.addAtHead(val)
            return None
        cursor = self.linked_list
        while cursor.next:
            cursor = cursor.next
        
        cursor.next = new_node
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        ll_size = 1 #we start at 1 
        if not index:
            self.addAtHead(val)
            return None
        
        if self.get(index) == -1 and self.get(index-1) == -1 : #outside of bounds
            return None
        
        cursor = self.linked_list
        for _ in range(index-1):
            cursor = cursor.next
        #insert here
        new_node.next = cursor.next 
        cursor.next = new_node

            
        

    def deleteAtIndex(self, index: int) -> None:
        
        if self.linked_list is None:
            return None
        
        if not index:
            self.linked_list = self.linked_list.next
            return None
        
        if self.get(index) != -1 and self.get(index-1) != -1:
            prev_node = self.linked_list
            next_node = self.linked_list.next
            for _ in range(index-1):
                prev_node = next_node
                next_node = next_node.next
            
            prev_node.next = next_node.next
                
                    
                
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)