import threading 
#this is for python 3.0 and aove. use import thread for python2.0 versions
from threading import*
import time

d={} #'d' is the dictionary in which we store data

#for create operation 
#use syntax "create(key_name,value,timeout_value)" timeout is optional you can continue by passing two arguments without timeout

def create(key,value,timeout=0):
    if key in d:
        print("Error: Key already exists") #Error message1
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): #constraints for file size less than 1GB and Jasonobject value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: #constraints for input key_name capped at 32chars
                    d[key]=l
                    print("Success :Key created")
                else:
                    print("Error:Invalid Key , Key size must be smaller than 32")
            else:
                print("Error: Memory limit exceeded!! ")#Error message2
        else:
            print("Error: Invalid key_name!! key_name must contain only alphabets and no special characters or numbers")#Error message3

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in d:
        print("Error: Key does not exist in database. Please enter a valid key or create one !") #Error message4
    else:
        value=d[key]
        if value[1]!=0:
            if time.time()<value[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(value[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                print(stri)
            else:
                print("Error: time-to-live of ",key,"has expired") #Error message5
        else:
            stri=str(key)+":"+str(value[0])
            print(stri)

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in d:
        print("Error: Key does not exist in database. Please enter a valid key or first create one") #Error message4
    else:
        value=d[key]
        if value[1]!=0:
            if time.time()<value[1]: #comparing the current time with expiry time
                del d[key]
                print("Success :Key deleted")
            else:
                print("Error: time-to-live of",key,"has expired") #Error message5
        else:
            del d[key]
            print("Success :Key deleted")

#I have an additional operation of modify in order to change the value of key before its expiry time if provided

#for modify operation 
#use syntax "modify(key_name,new_value)"

def modify(key,new_value):
    value=d[key]
    if value[1]!=0:
        if time.time()<value[1]:
            if key not in d:
                print("Error: given key does not exist in database. Please enter a valid key") #Error message6
            else:
                l=[]
                l.append(new_value)
                l.append(value[1])
                d[key]=l
                print("Success :Key modified")
        else:
            print("Error: time-to-live of",key,"has expired") #Error message5
    else:
        if key not in d:
            print("Error: given key does not exist in database. Please enter a valid key") #Error message6
        else:
            l=[]
            l.append(new_value)
            l.append(value[1])
            d[key]=l
            print("Success :Key modified")