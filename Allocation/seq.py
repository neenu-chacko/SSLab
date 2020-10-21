
'''
SEQUENTIAL MEMORY ALLOCATION
'''

f=[0]*50
 
while(1):
 count=0;
 print("The memory space can be represented as:")
 print("\n")
 print(f)

 print("To allocate files in sequential method:\n")
 print("Enter starting block and length of file to be allocated : ")
 start=int(input())
 length=int(input())
 for k in range(start,start+length):
     if(f[k]==0):
         count+=1
 if(length==count):
     for j in range(start,start+length):
         if(f[j]==0):
             f[j]=1
             print(j,end=' ')
             print(f[j])
     if(j!=(start+length-1)):
         print("The file has been successfully allocated")
 else:
     print("The block is already occupied, file not allocated")
  
 print("˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜˜ ")
 print("Do you want to enter more files? Enter 1 for Yes 0 for No")
 ch=int(input())
 if(ch==0):
     exit()


