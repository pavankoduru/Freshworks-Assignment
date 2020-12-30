#Run the kvdatastore.py and import it as a mkv
import kvdatastore as mkv  #importing as library

mkv.create("pavan",21)#creating without time-to-live

mkv.create("nec",40,5)#creating with time-to-live as 5 sec

mkv.read("nec") #accessing with-in 5 sec will return value

#wait for 10 sec and again access

mkv.read("nec") # shows error

mkv.read("pavan") # will return value 

mkv.create("pavan",30)#shows error

mkv.delete("pavan") #will delete the key and value

mkv.create(123,45) # shows error: wrong key type

#using multiple threads
thread1=Thread(target=(create or read or delete),args=(key,value,timeout)))
thread1.start()
thread1.sleep()

thread2=Thread(target=(create or read or delete),args=(key,value,timeout)))
thread2.start()
thread2.sleep()
#like this we can create and run multiple no of threads and it is thread safe

#other errors

#if key doesn't exists or previously delted
#if file memory limit exceeds 1GB

