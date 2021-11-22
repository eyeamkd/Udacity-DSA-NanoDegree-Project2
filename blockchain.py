import hashlib  
import datetime

class Block: 
    
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash() 
      self.next = None

    def calc_hash(self, input:str):
        sha = hashlib.sha256()
        sha.update(input.encode("utf-8")) 
        return sha.hexdigest() 
    
class BlockChain:
    
    head: Block 
    current: Block
    
    def __init__(self,value) -> None: 
        headBlock = self.add(value) 
        head = headBlock
    
    def add(self, data): 
        timestamp = datetime.timestamp()
        block = Block(timestamp,data, self.current.hash) 
        self.current = block 
    
    def __repr__(self) -> str: 
        temp = self.head
        while(temp.next is not None):
            print(temp.data, "--->",end="") 
            temp = temp.next 
        
            
        
        
        
    
