_group_dict = {} 

class Group(object): 
        
    def __init__(self, _name):
        self.name = _name
        self.groups = [] 
        self.users = []
    
    def add_group(self,group):
        self.groups.append(group)  
        
    def add_user(self,user):
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
        return False 

#test case

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user) 
parent.add_user("parent_user")

child.add_group(sub_child)
parent.add_group(child)  

print(is_user_in_group("parent_user",sub_child))


 
        
        
        
        
        