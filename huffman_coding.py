import sys 

class Huffman_Node:
    def __init__(self, character:str="", frequency:int=0) -> None: 
        self.leftNode = Huffman_Node("",0)
        self.rightNode = Huffman_Node("",0) 
        self.character = character 
        self.frequency = frequency 
        pass  
    
    def getCharacter(self):
        return self.character 
    
    def getFrequency(self):
        return self.frequency 
    
    def getLeftNode(self):
        return self.leftNode
    
    def getRightNode(self):
        return self.rightNode
        

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
        queue = []
        for letter in frequency_dictionary.keys(): 
            node = Huffman_Node(letter,frequency_dictionary[letter]) 
            queue.append(node) 
        return queue
     
def huffman_encoding(string :str): 
    frequency_dictionary = determine_frequency(string)   
    priority_queue = create_priority_queue(frequency_dictionary) 
    
   

def huffman_decoding():
    pass  

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word" 
    
    print(result)  
    
    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))