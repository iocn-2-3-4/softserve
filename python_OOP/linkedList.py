class Node(object):
 
    def __init__(self, data, next):
        self.data = data
        self.next = next
 
 
class linkedList(object):
 
    head = None
    tail = None
 
    # def get(self):
    #     current_node = self.head
    #     while current_node is not None:
    #         return current_node.data,
    #         current_node = current_node.next
    #     # print None

    def get(self):
        s = " "
        current_node = self.head
        if current_node != None:
            while current_node.next != None:
                s += str(current_node.data) + " "
                current_node = current_node.next
            s += str(current_node.data) + " "
        return s
 
    def put(self, data):
        node = Node(data, None)
        # node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node
 
    def delete(self, node_value):
        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.data == node_value:
               
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    self.head = current_node.next

            previous_node = current_node
            current_node = current_node.next

    def size(self):
        temp = self.head 
        count = 0 
        while (temp):
            count += 1
            temp = temp.next
        print count
        return count

    def indexOf(self, item):
        index = 1
        current = self.head
        found = False
        while current != None:
            if current.data == item:
                found = True
                break
            else:
                current = current.next
                index += 1
        if not found:
            index = None
        print index
        return index
        
        

# s = linkedList()
# s.put("test1")
# s.put("test2")
# s.put(89)
# s.put(111)
# s.size()
# print " "
# s.indexOf(111)
# print " "
# print s.get()
# s.delete(2)
# print " "
# print s.get()
# print " "
# s.size()
