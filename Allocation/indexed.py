# INDEXED ALLOCATION
f = [0]*50
index = [0]*50
count = 0
def alloc():
        count = 0
        for i in range(n):
            print("Enter the next index:")
            index[i] = int(input())
            if(f[index[i]]==0):
                count+=1
            else:
                    print(" Already allocated index" )
                    return
        if(count==n):
            for i in range(n):
                f[index[i]]=1
            print("Allocated\nFile Indexed\n")
            for k in range(n):
                print(ind,"---->",index[k],":",f[index[k]])
        else:
            print("File in index is already allocated")
            print("Enter another file index")
            alloc()
while(1):
   
    print("\n")
    ind = int(input("Enter the index block :"))
    if(f[ind]==0):
        n = int(input("Enter the number of files on the index :"))
        alloc()
    else:
        print("Index block is allocated")
    print("------------------------------------------------------ ")    
    print("Do you want to enter more file(Yes - 1/No - 0)")
    c = int(input())
    if(c==0):
        exit()


        
