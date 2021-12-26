# Explanation for the active directory problem

The solution mainly revolves around the essence of the beautiful data structure called "set" in python

set is such a data structure which doesn't hold multiple elements of the same type, and this actually comes in handy while doing "union" and "intersection" computations

adding elements to the set, irrespective of the elements are repeated, would give a union of the elements. 

for intersection, I would just add all the elements in a set called as "common" and then check for repeated elements by traversing the other set. 
If the element turned out to be repeated, then I'd add that element into a linkedlist, I'm avoiding the repeatition here by removing the element from the common set once if it's added to the list

## Time Complexity:

intersection():
The function goes through a while loop until it traverses the list1, lets say that the number of elements present in the list1 are L, then the time complexity is O(L)

It has another while loop, which also does the same traversal but on the second list, lets say that the number of elements present in the second list are M, then the time complexity is O(M)

Since, we're dealing with LinkedList, the addition and removal functions have O(1) time complexity 

Therefore, the total time complexity for this function is 
O(L) + O(M)

union():
The union function has while loop that executes for all the elements present in the LinkedLists 1 and 2. 
Therefore this would account for the time complexity of 
O(G), where G is max of L1 and L2 
Second for loop executes for the number of elements present in the union set, which lets say is K, hence the time complexity is O(K)
Therefore the total time complexity of this union function is O(G) + O(K) 


Space Complexity: 

Union: O(n) where 'n' is the number of elements formed after unionization of two lists 

Intersection: O(k) where 'k' is the number of common elements present.