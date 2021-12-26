# remove least recently used entry value 

# getting the element or setting the element both are considered to be "used operations " 

# get returns element if present else returns -1 


class LRU_Cache(object): 
    
    capacity = 0 
    cache = {}  
    min_hit_element = None
    # minimum hit element can be stored so as to easily remove it
    # key:{value:,hits:}
    
    def __init__(self, capacity) -> None:  
        if(capacity == 0):
            raise ValueError 
        self.capacity = capacity
        super().__init__() 
    
    def get(self, key):  
        try:
            value =  self.cache[key]["value"];  
            self.cache[key]["hits"]+=1 
            return value
        except KeyError as e:
            return -1        
        
    def set(self,key,value):  
        #if capacity is 5, run remove function 
        if(self.capacity != -1):
            if(len(self.cache)==self.capacity):
                self.__remove_element()
        self.cache[key] = {"value":value,"hits":0}; 
    
    # def get_min_hit_element():
    #     for element in self.cache:
    #         if(self.cache[element]["hits"]<minHit): 
    #             minHit = self.cache[element]["hits"]
    #             key = element
                
    
    def __remove_element(self):  
        minHit = 9999;
        key = '';
        for element in self.cache:
            if(self.cache[element]["hits"]<minHit): 
                minHit = self.cache[element]["hits"]
                key = element
        self.cache.pop(key) 


#test case
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);  

print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9)) 
our_cache.set(5, 5)   
# print(sorted(our_cache.cache.values(), key=lambda element: element["hits"]))  
# first = list(our_cache.cache.keys())[0]
# print(first)
our_cache.set(6, 6)  
print(our_cache.get(3)) 

our_cache = LRU_Cache(0) # Throws Value Error 

our_cache = LRU_Cache(-1) # Can add infinite numbers ( Obv RAM limit :P)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);   
our_cache.set(5, 5);
our_cache.set(6, 6);
our_cache.set(7, 7);
our_cache.set(8, 8);   
print(our_cache.get(7))