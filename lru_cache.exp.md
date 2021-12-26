# Explnation for LRU Cache

Created a Cache Class, which holds the current cache capacity and a dictionary that stores record of all the values that are currently present in cache

The reason for having both of these separately is that, I didn't want to waste essential compute time in cacluating the length of dictionary everytime I wanted to know if the cache capacity is reached  

Each record in the dictionary holds the property "hits", which shows how many times has the element being accessed.
Which gets incremented for the every "set"

The primary logic being, for every element that's added to the cache, I check if it's impacting the capacity of the cache, if it is then I get the element which has least number of hits and remove it from the dictionary thereby making space for the cache

Cache returns "-1" for any element that was not present in the cache but was requested

## Time Complexity:

get(): since this function is searching for the element in the dictionary, which is nothing but a Hash Table, we know that the search time in a HashTable is O(1), hence the time complexity of this function is O(1)

set():
This calls remove_element() function ONLY if the capacity is reached, so, O(1) for checking and the removal_element() checks all the elements for getting the min hit element
therefore the time complexity would be O(N), where 'N' is equal to the number of elements in the cache
Hence, what we see here is a amortized time complexity which is dependent on the capacity of the Cache
Until the Cache reaches the capacity, the time complexity is O(1), after that depending on the amount of elements removed the time complexity changes, here being O(N) 


## Space Complexity: 

get():  The get function has the space complexity of O(1) since we're just returning the elements

set(): The set function has the space complexity of O(n) since we're adding the elements into the cache. 
Where 'n' is the number of elements in the cache