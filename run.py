#here are the commands to demonstrate how to access and perform operations on a main file


#run the MODULE of MAIN FILE and import mainfile as a library 

import threading
import time
import mainfile as operation 
#importing the main file("mainfile" is the name of the file I have used) as a library 


operation.create("A",1)
#to create a key with key_name,value given and with no time-to-live property


operation.create("B",2,0.0000001) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


operation.read("A")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


operation.read("B")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EoperationPIRED else it returns an ERROR


operation.create("A",3)
#it returns an ERROR since the key_name already exists in the database
#To overcome this error 
#either use modify operation to change the value of a key
#or use delete operation and recreate it


operation.modify("A",3)
#it replaces the initial value of the respective key with new value 

 
operation.read("A")
#it deletes the respective key and its value from the database(memory is also freed)


try:
	t1=threading.Thread(target=(operation.create),args=("C",4,3)) #as per the operation
	t1.start()
	t2=threading.Thread(target=(operation.create),args=("D",5)) #as per the operation
	t2.start()
except:
   print("Error: unable to start thread")

print()
operation.read("D")

#the code also returns other errors like 
#"invalidkey" if key_length is greater than 32 or key_name contains any numeric,special characters etc.,
#"key doesnot exist" if key_name was mis-spelt or deleted earlier
#"File memory limit reached" if file memory exceeds 1GB
