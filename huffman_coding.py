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
    
    def merge(self, otherNode): 
        new_node = Huffman_Node("",self.frequency + otherNode.frequency)  
        if(self.frequency<=otherNode.frequency):
            new_node.insertLeft(self) 
            new_node.insertRight(otherNode) 
        else: 
            new_node.insertLeft(otherNode)
            new_node.insertRight(self) 
        return new_node


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
        print("Lowest prirority", queue.get())
        return queue
     
def huffman_encoding(string :str): 
    frequency_dictionary = determine_frequency(string)   
    priority_queue = create_priority_queue(frequency_dictionary) 
    root_node = build_huffman_tree(priority_queue)  
    generate_encoded_data(root_node,'')
    print("The root node is here", root_node)

def lowest_frequency_nodes(queue): 
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
        print("Combined frequency of the merged nodes is", merged_node.frequency)
        queue.put(PrioritizedItem(merged_node.frequency,merged_node)) 
    
    return queue.get().item
    
def generate_encoded_data(root_node:Huffman_Node, code):  
    # doing BFS   
    if(root_node.node_type =='parent'):
        generate_encoded_data(root_node.leftNode,code=code+'0')
        generate_encoded_data(root_node.rightNode, code=code+'1')
    print('code is', code, "Frequency is", root_node.frequency)

def huffman_decoding():
    pass  

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word" 
    
    queue = huffman_encoding(a_great_sentence)
