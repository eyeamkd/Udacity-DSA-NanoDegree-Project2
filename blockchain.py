import hashlib

class BlockChain:

    def calc_hash(slef, input:str):
        sha = hashlib.sha256()
        sha.update(input.encode("utf-8")) 
        return sha.hexdigest()


blockchain = BlockChain() 

result = blockchain.calc_hash("Kunal Dubey")
        
print(result)