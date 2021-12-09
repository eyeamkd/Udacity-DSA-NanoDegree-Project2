# File Recursion Explanation

The main component of this solution lies in the recursive_search function, that takes in path and the list as it's arguments. 
Where "path" is just a file path and the list is a empty directory that's passed along multiple recursive calls inorder to add items into it

recursive_search() uses the "os" module to determine if the paht is of a directory, if it is then is dives into the directory to fetch the paths of each file present in it, as it constructs the active file path the function is recursively called again to determine if it's a directory. 

Once all the paths are collected, a simple substring search would return all the paths with the extension desired