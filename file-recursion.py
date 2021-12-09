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
    paths = [] 
    realPath = os.path.realpath(path)
    dirlist = recursive_search(realPath,paths) 
    for path in dirlist:
        if(suffix in path):
            print(path)

#test
find_files('.c',testpath)