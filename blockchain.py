import hashlib  
import time

class Block: 
    
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data) 
      self.next = None

    def calc_hash(self, input:str): 
        input = str(input)
        sha = hashlib.sha256()
        sha.update(input.encode("utf-8")) 
        return sha.hexdigest() 
    
class BlockChain:
    
    head: Block 
    current: Block 
    prev:Block
    
    def __init__(self,value) -> None:  
        headBlock = Block(time.time(),value,None)
        self.head = headBlock
        self.current = self.head
        self.head.next = self.current
        
    
    def add(self, data): 
        timestamp = time.time() 
        block = Block(timestamp,data, self.current.hash)  
        self.current.next = block 
        self.current = block
    
    def __repr__(self) -> str: 
        temp = self.head 
        chain = ""
        while(temp.next is not None): 
            chain +="{} -->".format(temp.data)
            temp = temp.next  
        chain+="{}".format(temp.data) 
        return chain
blockchain = BlockChain(8)
blockchain.add(7)
blockchain.add(9) 

print(blockchain)

        
            
        
        
        
    
