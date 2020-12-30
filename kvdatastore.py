from threading import *
import time
dictionary={}#used to store in key:value format
def create(key,val,timeout=None):
    if key in dictionary:
        print("Error!-key already exists")
    else:
        if key.isalpha():
            if len(key)<=32:
                if len(dictionary)<(1024**3) and val<=(16*1024**2):
                    if timeout==None:
                        dictionary[key]=[val,0] #for timeout as 0
                    else:
                        dictionary[key]=[val,time.time()+timeout]
                
                else:
                    print("Memory Limit Exceeded!,Check again")
            else:
                print("keylength must be less than 32 ")
        else:
            print("Invalid key name: Value of key must be only Alphabets!")
def read(key):
    if key not in dictionary:
        print("Key doesn't exists!pls enter a valid key")
    else:
        v=dictionary[key]
        if v[1]==0:
            return "{}:{}".format(key,v[0])
        else:
            if time.time()<v[1]:
                return "{}:{}".format(key,v[0])
            else:
                print("Error! : Time-to-live of given key has expired")
                del dictionary[key]
def delete(key):
    if key not in dictionary:
        print("Key doesn't exists!pls enter a valid key")
    else:
        v=dictionary[key]
        if v[1]==0:
            del dictionary[key]
            print("Given {} succesfully deleted...".format(key))
        else:
            if time.time()<v[1]:
                del dictionary[key]
                print("Given {} succesfully deleted...".format(key))
            else:
                print("Error! : Time-to-live of given key has expired")
        
        
            
        
            

