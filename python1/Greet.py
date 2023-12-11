import time
timestamp= input(time.strftime('%H:%M:%S'))
print(timestamp)
timestamp= time.strftime('%H')
print(timestamp)
timestamp= time.strftime('%M')
print(timestamp)
timestamp= time.strftime('%S')
print(timestamp)
if(time.strftime('%H:%M:%S')>'00:00:00' and time.strftime('%H:%M:%S')<='12:00:00'):
    print("gm")
elif(time.strftime('%H:%M:%S')>'12:00:00' and time.strftime('%H:%M:%S')<='16:00:00'):
    print("ga")   
elif(time.strftime('%H:%M:%S')>'16:00:00' and time.strftime('%H:%M:%S')<='18:00:00'):
    print("ge")     
elif(time.strftime('%H:%M:%S')>'18:00:00' and time.strftime('%H:%M:%S')<='24:00:00'):
    print("gn")
else:
    print("time to say good bye")         




