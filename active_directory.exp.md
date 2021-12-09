# Explanation for the active directory problem 

The solution mainly revolves around the essence of the beautiful data structure called "set" in python

set is such a data structure which doesn't hold multiple elements of the same type, and this actually comes in handy while doing "union" and "intersection" computations

adding elements to the set, irrespective of the elements are repeated, would give a union of the elements. 

for intersection, I would just add all the elements in a set called as "common" and then check for repeated elements by traversing the other set. 
If the element turned out to be repeated, then I'd add that element into a linkedlist, I'm avoiding the repeatition here by removing the element from the common set once if it's added to the list