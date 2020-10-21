full,x = 0,0
empty=int(input("Enter size of buffer:"))
mutex=1
y=1
def wait(s):
    while(s<=0):
        pass
    s-=1
    return(s)
def signal(s):
    s=s+1
    return(s)
def producer():
    global full,empty,mutex,x
    mutex=wait(mutex)
    full=signal(full)
    empty=wait(empty)
    x=x+1
    
    print(f"\nItem {x} Produced\n")
    mutex=signal(mutex)
def consumer():
    global full,empty,mutex,x,y
    mutex=wait(mutex)
    full=wait(full)
    empty=signal(empty)
    print(f"\nConsumer consumes Item {y}\n")
    y=y+1
   
    x=x-1
    mutex=signal(mutex)
print("\n1.Produce \n2.Consume\n3.Exit")
while(1):
    ch=int(input("Enter the choice:"))
    if(ch==1):
        if((mutex==1) and (empty!=0)):
            producer()
        else:
            print("\nBuffer is FULL! Wait till a product is consumed.\n")
    elif(ch==2):
        if((mutex==1) and (full!=0)):
            consumer()
        else:
            print("\nBuffer is Empty!Wait for product to be produced.\n")        
    else:
        exit()

