

pages = [0]*50
n = int(input("Enter the number of blocks already allocated\n"))
print("Enter allocated block numbers:")
for i in range(n):
    a=int(input())
    pages[a]=1
while(1):
    print(pages)
    print("Enter starting block of file to be allocated:\n")
    start = int(input())
    print("Enter the length of file to be allocated:\n")
    length = int(input())
    k = length
    if(pages[start]==0):
        j=start
        while(j<start+k):
            if (pages[j]==0):
                 pages[j]=1
                 print(j,' -> ',pages[j])
            else:
                k=k+1
                print(j,'Block is already allocated\n')
            j+=1    
    else:
     print("Starting block is already allocated\n")
    print("-----------------------------------------------------------")    
    print("Do you want to continue?\nEnter 1 for yes, 0 for no")
    ch = int(input())
    if(ch==0):
        exit()

