dir=['']*50
x=0
rear=0
def search(name):
    if name in dir:
        return(1)
dirname=input("Enter the directory name: ")
while(1):
    count=0
    cd=0
    print("Choose your Option: \n 1.Add a file \n 2.Delete a file \n 3.Search file \n 4.Display files \n 5.Exit\n")
    ch=int(input())
    if(ch==1):
        fname=input("Enter filename: ")
        s=search(fname)
        if(s):
            print("Filename already exists")
        else:
          dir[rear]=fname
          rear+=1
    elif(ch==2):
        dname=input("\n Enter filename:")
        for i in range(rear):
            if(dir[i]==dname):
                dir[i]=''
                cd+=1
        if(cd==0):
            print("File Not Found!\n")
    elif(ch==3):
        dname=input("\n Enter filename:")
        for i in range(rear):
            if(dir[i]==dname):
                print("File found at position",i)
            else:
                x=x+1
        if(x==rear):
            print("File Not Found!\n") 
    elif(ch==4):
        print("--------------------------------")
        print("The files in directory",dirname,end='')
        print(" are listed below:")
        for i in range(rear):
            if(dir[i]!=''):
                print("-->",end='')
                print(dir[i])
                count+=1
        if(count==0):
            print(" No Files Found ")
        print("--------------------------------")
    else:
        exit();    

