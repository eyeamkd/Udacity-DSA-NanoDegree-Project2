# Explnation for the BlockChain Problem 

Every block is a class, since it's a repeated entity with specific properties 

Every block has the properties of 
- timestamp
- data
- hash
- next block

BlockChain is a class that contains list of blocks 

At a given timeframe, we can traverse through the blockChain using the head block and calling on the next property of the head block 

I've also created a method to add more blocks using the "add" method 

## Time Complexity 

add() function takes O(1) to calculate time, create a Block object and then adding the created block to the chain 
Hence, add() function's time complexity is O(1) 

print() however goes through all the blocks present in the blockchain, hence in order to print all the blocks, it shall cost us a complexity of O(B), where B is the number of blocks present "on-chain"

## Space Complexity 

BlockChain():  
O(n) space time complexity is the order of growth of space required to create a block chain.
Where 'n' is the number of blocks present in the block chain

add(): 
O(1) is the space complexity required to add blocks on to the BlockChain