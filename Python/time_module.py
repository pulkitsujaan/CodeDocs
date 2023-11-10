import time
a=0
initial=time.time()
while(a<5):
    print("Hello World")
    # print(time.time()-initial)
    time.sleep(2)
    a+=1
print(time.asctime(time.localtime(time.time())))