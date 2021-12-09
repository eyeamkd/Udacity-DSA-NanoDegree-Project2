import sys 
from queue import PriorityQueue 
from dataclasses import dataclass, field
from typing import Any

class Huffman_Node:  
    node_type:str 
    frequency:int
    
    def __init__(self, frequency, type, data=None) -> None: 
        self.frequency = frequency
        self.node_type = type 
        self.data = data
        pass  
    
    def getData(self):
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
    
   


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)
        

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
            node = Huffman_Node(frequency_dictionary[letter],'leaf',letter)
            queue.put(PrioritizedItem(frequency_dictionary[letter],node))
        # print("Lowest prirority", queue.get())
        return queue
     
def huffman_encoding(string :str): 
    frequency_dictionary = determine_frequency(string)   
    #print("Frequency Dictionary is",frequency_dictionary) 
    priority_queue = create_priority_queue(frequency_dictionary) 
    root_node = build_huffman_tree(priority_queue) 
    generate_encoded_data(root_node,'',frequency_dictionary) 
    #print("Modified dictionary is", frequency_dictionary) 
    encoded_string = '' 
    for letter in string:
        encoded_string = encoded_string + frequency_dictionary[letter]['code']  
    #print("Encoded string is",encoded_string) 
    return encoded_string,root_node
    
    #print("The root node is here", root_node) 

def lowest_frequency_nodes(queue): 
    #print("Queue is",queue.queue)
    return queue.get(), queue.get()
    pass 

def merge(node1:PrioritizedItem, node2:PrioritizedItem): 
    total_frequency = node1.priority + node2.priority
    merged_node = Huffman_Node(total_frequency,'parent') 
    merged_node.leftNode = node1.item    
    merged_node.rightNode = node2.item
    return merged_node 
    
    
def build_huffman_tree(queue:PriorityQueue): 
    while(queue.qsize()>1):
        node1, node2 = lowest_frequency_nodes(queue) 
        merged_node = merge(node1, node2)  
        #print("Combined frequency of the merged nodes is", node1.item.data, node2.item.data)
        queue.put(PrioritizedItem(merged_node.frequency,merged_node)) 
    
    return queue.get().item
    
def generate_encoded_data(root_node:Huffman_Node, code,dict):  
    # doing BFS   
    if(root_node.node_type =='parent'): 
        left_code = code+'0'
        right_code = code+'1'
        generate_encoded_data(root_node.leftNode,left_code,dict)
        generate_encoded_data(root_node.rightNode,right_code,dict) 
    elif(root_node.node_type == 'leaf'):
        frequency = dict[root_node.data]   
        dict[root_node.data] = {'code':code, 'frequency':frequency}
        return code,root_node.data

def huffman_decoding(encoded_string,root_node:Huffman_Node):
    decoded_string = ''  
    #print("Root node is",root_node)
    temp_root:Huffman_Node = root_node
    for bit in encoded_string:
        if(bit=='0'): 
            temp_root = temp_root.leftNode  
            if(temp_root.node_type == 'leaf'):
                #print("temp root is", temp_root.node_type)
                decoded_string = decoded_string + temp_root.data
                temp_root = root_node 
        elif(bit =='1'):
             temp_root = temp_root.rightNode 
             if(temp_root.node_type == 'leaf'):
                decoded_string = decoded_string + temp_root.data
                temp_root = root_node 
    print("Decoded string is", decoded_string)
    return decoded_string
        



# test case

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "AAAAAAABBBCCCCCCCDDEEEEEE" 
    
    encoded_string,root_node = huffman_encoding(a_great_sentence)  
    decoded_string = huffman_decoding(encoded_string,root_node)
    print(encoded_string) 
    print(decoded_string)
