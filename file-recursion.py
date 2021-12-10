import os 

testpath = './testdir'
# suffix is extension  

def recursive_search(path,list):
    list.append(path)
    if(os.path.isdir(path)): 
        dirlist = os.listdir(path) 
        for dir in dirlist:  
            realPath = os.path.realpath(path+'/'+dir) 
            recursive_search(realPath,list) 
    return list  

def find_files(suffix,path): 
    if(len(suffix)==0 or len(path)==0):
        raise ValueError("Arguments cannot be empty")
    if(type(suffix)!=str or type(path)!=str):
        raise ValueError("Kindly enter only string arguments")
    paths = []  
    flag = True
    realPath = os.path.realpath(path)
    dirlist = recursive_search(realPath,paths) 
    for path in dirlist:
        if(suffix in path): 
            flag = False
            print(path) 
    if(flag):
        print("File with the ",suffix," extension not found on the path",path)

#test
find_files('.c',testpath) 
find_files('',testpath) #raises value error
find_files(1,testpath) #raises value error 
find_files('.f',testpath) #reutrns file not found message 
