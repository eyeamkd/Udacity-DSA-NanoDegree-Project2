# Explnation for LRU Cache

Created a Cache Class, which holds the current cache capacity and a dictionary that stores record of all the values that are currently present in cache

The reason for having both of these separately is that, I didn't want to waste essential compute time in cacluating the length of dictionary everytime I wanted to know if the cache capacity is reached  

Each record in the dictionary holds the property "hits", which shows how many times has the element being accessed. 
Which gets incremented for the every "set" 

The primary logic being, for every element that's added to the cache, I check if it's impacting the capacity of the cache, if it is then I get the element which has least number of hits and remove it from the dictionary thereby making space for the cache 

Cache returns "-1" for any element that was not present in the cache but was requested 
