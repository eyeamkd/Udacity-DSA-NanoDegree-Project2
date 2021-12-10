_group_dict = {} 

class Group(object): 
        
    def __init__(self, _name): 
        if(len(_name)==0):
            raise ValueError("Group name cannot be empty")
        self.name = _name
        self.groups = [] 
        self.users = []
    
    def add_group(self,group):
        self.groups.append(group)  
        
    def add_user(self,user): 
        if(len(user)==0):
            raise ValueError("User name cannot be empty")
        self.users.append(user) 
        _group_dict[user] = self.name
    
    def get_groups(self):
        return self.groups 

    def get_users(self):
        return self.users 
    
def is_user_in_group(user,group):  
    if(_group_dict[user]):
        if(_group_dict[user]==group.name):
            return True
        return False,"User not found" 

#test cases

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild") 
empty_group = Group("") #raises error


sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user) 
parent.add_user("parent_user") 
parent.add_user("") #raises error

child.add_group(sub_child)
parent.add_group(child)  

print(is_user_in_group("parent_user",sub_child))


 
        
        
        
        
        