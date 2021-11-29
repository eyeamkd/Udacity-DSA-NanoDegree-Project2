import sys 


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

def huffman_encoding(): 

    pass 

def huffman_decoding():
    pass  

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word" 
    result = determine_frequency(a_great_sentence) 
    print(result)  
    
    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))