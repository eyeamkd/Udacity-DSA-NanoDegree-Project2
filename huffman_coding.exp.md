# Explanation of Huffman coding 

This was by far my the most interesting problem so far. 

To solve this, I wrote a "Huffman_Node" class, which kinda acted like a linkedList node, and since I'm kinda writing it from scratch, I thought why don't I add the problem specific properties in it ( this was my "Aha" moment ) and then use those properties wherever requried 

Explaining the functions: 

The solution starts by accepting a string as an input and passing it through "huffman_encoding()" function 

*huffman_encoding()* function then calls *determine_frequency()* which just traverses the string and builds a dictionary to store the frequency of the letters present in the string 

the dictionary is then passed into a function called *"create_priority_queue()* which creates a priority queue based on the frequency of the letter present in the dictionary, it takes in each element in the dictionary and creates a Huffman_Node out of it, 
- where the  node_type is "leaf" (as all the nodes which have data are leaf nodes in a huffman tree) 
- the data is the letter associated
- frequency is the amount of times the letter is repeated 

The queue created is then passed to the function *build_huffman_tree()* 
which deques the elements based on their priority and merges them into a Huffman_node but this time of the type "parent" this process continues until the queue is left with only one single element which turns out to be our "Root Node" 

This root_node is then passed to the *"generate_encoded_data()"* function to do exactly what is says, i.e generate encoded data out of the huffman tree that was just built 
The function also takes in a empty string, which gets passed on to every recursive call and gets populated with the encoded data 
The last parameter to this function is the dictionary which was already created above, this is because every letter (key) could then be easily mapped to the code associated with it, ( we'll know why in a minute ) 

The above function manipulates the dictionary with each letter having it's own encoded code. 
The initial string is then traversed to replace the letter with the code that was generated. 
and the encoded string is then returned. 

*huffman_decoding()* function takes in the encoded string and the root node. 
The root node of the created huffman tree is then traversed according to the bit value present in the encoded string, and as the traversal reaches a node of type "leaf" we append the data present init to a string. 
Atlast this string is returned, which then has decoded value.  


Time Complexity:

For the huffman_encoding() function: 
determine_frequency() function loops through the letters in the string, hence has a time complexity of O(n), where 'n' is the length of the string  

create_priority_queue() loops through the number of keys in the dictionary which is "k", hence the time complexity is O(k), where inserting element into the queue and creating a node can be considered as O(1) operations 

build_huffman_tree() loops through the number of items present in the queue which is 'k',hence the time compelxity is O(k). Considering the merging and creation of Huffman nodes to be O(1). 

generate_encoded_data() is a recursive function and the time complexity here depends on the number of nodes that are present, since it is 'k', the time complexity here is also O(k)

Therefore the total time complexity for huffman_encoding() is O(n) + O(k) + O(k) + O(k), which is O(n) + 3O(k) 
since, constants can be ignored, we have O(n) + O(k) 

For huffman_decoding(): traversal for the number of bits, lets consider that to be 'b', then it's time complexity is O(b) 

Total Time Complexity for the execution of the program is: O(n) + O(k) + O(b) 
Where n,k,b are *dependent* on length of the string, number of items in the queue and the number of bits generated.
