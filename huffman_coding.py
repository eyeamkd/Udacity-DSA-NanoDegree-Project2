import sys 
from queue import PriorityQueue 
from typing import Any

class Huffman_Node: 
    def __init__(self, data) -> None: 
        self.data = data 
        pass  
    
    def getCharacter(self):
        return self.data  
    
    def insertLeft(self, node):
        self.leftNode = node 
        return 
    
    def insertRight(self, node):
        self.rightNode = node
        return 
    
    def getFrequency(self):
        return self.frequency 
    
    def getLeftNode(self):
        return self.leftNode
    
    def getRightNode(self):
        return self.rightNode   
    
    def merge(self, otherNode): 
        new_node = Huffman_Node("",self.frequency + otherNode.frequency)  
        if(self.frequency<=otherNode.frequency):
            new_node.insertLeft(self) 
            new_node.insertRight(otherNode) 
        else: 
            new_node.insertLeft(otherNode)
            new_node.insertRight(self) 
        return new_node

class PrioritizedItem:
    priority: int
    item : Any
    def __init__(self, priority, item) -> None:
        self.priority = priority 
        self.item = item 
        
class Heap_node: 
    
    def __init__(self,value) -> None: 
        self.value = value
        self.leftNode = None 
        self.rightNode = None  
    
    def insertLeft(self,node):
        self.leftNode = node
    
    def insertRight(self,node):
        self.rightNode = node 
    
    def getLeft(self):
        return self.leftNode 
    
    def getRight(self):
        return self.rightNode 

class priority_queue:
    
    def __init__(self,value, order="ASC") -> None: 
        self.root = Heap_node(value)
        self.size = 0 
        self.order = order
    
    def size(self):
        return self.size 
    
    def insert(self,value):   
        #CHALLENGE: IMAGINE A COMPLETE BINARY HEAP, 
        # AND THEN SUDDENLY YOU GOT TO INTRODUCE A NODE 
        # WHICH WOULD MEAN TRAVERSING THE TREE AND REPLACING THE ROOT
        pass
        


def determine_frequency(string:str): 
    dictionary = {} 
    string = string.replace(" ","") 
    # print("Stripped string is ", string);
    for letter in string:
        if(letter in dictionary.keys()):
            dictionary[letter]+=1 
        else:
            dictionary[letter]=1 
    return dictionary 

def create_priority_queue(frequency_dictionary:dict): 
        frequency_dictionary = dict(sorted(frequency_dictionary.items(), key=lambda item: item[1]))
        queue = PriorityQueue()
        for letter in frequency_dictionary.keys():  
            queue.put(PrioritizedItem(frequency_dictionary[letter],letter))
        print("Lowest prirority", queue.get())
        return queue
     
def huffman_encoding(string :str): 
    frequency_dictionary = determine_frequency(string)   
    priority_queue = create_priority_queue(frequency_dictionary) 
    root_node = build_huffman_tree(priority_queue) 
    print("The root node is here", root_node)
    # print("Lowest priority is", priority_queue.get()[1])
    # print(priority_queue) 

def lowest_frequency_nodes(queue): 
    return queue.get(), queue.get()
    pass 

def merge(node1, node2):
    total_frequency = node1[0] + node2[0] 
    merged_node = Huffman_Node(total_frequency) 
    merged_node.leftNode = Huffman_Node(node1[0]) 
    merged_node.rightNode = Huffman_Node(node2[0]) 
    return merged_node 
    
    
def build_huffman_tree(queue:PriorityQueue): 
    while(queue.qsize()!=1):
        node1, node2 = lowest_frequency_nodes(queue) 
        merged_node = merge(node1, node2)  
        print("Combined frequency of the merged nodes is", merged_node.data)
        queue.put(PrioritizedItem(merged_node.data,merged_node)) 
    
    return queue
         
        
    pass    


    
   

def huffman_decoding():
    pass  

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word" 
    
    queue = huffman_encoding(a_great_sentence)
    
    
    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))