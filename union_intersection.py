class Node: 
    
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList: 
    
    def __init__(self):
        self.head = None

    #overrides the print call
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1:LinkedList, llist_2:LinkedList)->LinkedList: 
    if(len(llist_1)==0 and len(llist_2)==0):
        raise ValueError("Empty lists cannot be unionized")
    union = set()
    unionList = LinkedList()  
    while(llist_1.head is not None or llist_2.head is not None):
        if(llist_1.head is not None):
            union.add(llist_1.head.value) 
            llist_1.head = llist_1.head.next
        if(llist_2.head is not None):
            union.add(llist_2.head.value)  
            llist_2.head = llist_2.head.next 
    for node in union:
        unionList.append(node)
    return unionList 
    

def intersection(llist_1, llist_2): 
    if(len(llist_1)==0 and len(llist_2)==0):
        raise ValueError("Empty lists cannot be intersected")
    common = set()    
    common_list: LinkedList = LinkedList();
    while(llist_1.head!=None):
        common.add(llist_1.head.value)
        llist_1.head = llist_1.head.next 
    while(llist_2.head!=None):
        if(llist_2.head.value in common): 
            common.remove(llist_2.head.value)
            common_list.append(llist_2.head.value)
        llist_2.head = llist_2.head.next 
    if(len(common_list)==0):
        return "No common element found" 
    return common_list
    


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

# print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i) 

print(linked_list_3) 
print(linked_list_4)
print("Intersection value")
print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4)) 


element_3 = []
element_4 = []
print (union(linked_list_3,linked_list_4)) #raises error
print (intersection(linked_list_3,linked_list_4)) #raises error


