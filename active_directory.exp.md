# Explanation for Union Intersection problem 

Created a Group class, inorder to make the code reusable 

added the functions: 

*add_group* which is used to add a group inside another group  
Time Complexity: O(1)
Space Complexity:  S(g), where 'g' is the amount of space required for one group


*add_user* which is used to add a user inside a group 
Time Complexity: O(1) 
Space Complexity: S(u), where 'u' is the amount of space required for one user


*get_groups* which is used to return all the groups inside a group 
Time Complexity: O(1) 
Space Complexity: S(1), since we're not storing and just returning the groups that are present


*get_users* which is used to return all the users inside a group 
Time Complexity: O(1) 
Space Complexity: S(1), since we're not storing and just returning the users that are present

*is_user_in_group* which is used to check if a user exists in a group 
Time Complexity: O(1) since the group_dict is a dictionary and the time complexity of getting an element from the dictionary is O(1)

Space Complexity: S(1) boolean value storage

Used to concept of normalization and Flattening objects to have a central dictionary that stores every users's information that way I don't have to go deep searching or also do recursive 



