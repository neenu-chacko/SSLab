class Directory:
    def __init__(self,name):
        self.name=name
        self.files=[]
        self.folders={}
    def createfile(self,file):
        if(file not in self.files):
            self.files.append(file)
            print(f"{file} has been created inside the directory {self.name}")
        else:
            print(f"{file} is already present in the directory")
    def createfolder(self,folder):
        if(folder not in self.folders):
            self.folders[folder.name] = folder
            print(f"\n{folder.name} has been created inside the directory {self.name}")
        else:
            print(f"\n{folder.name} is already present in the directory")
    def remove(self,item):
        if(item in self.files):
            self.files.remove(item)
            print(f"{item} has been removed from the directory {self.name}")
        elif(item in self.folders):
            self.folders.pop(item)
            print(f"{item} has been removed from the directory {self.name}")
        else:
            print("No such file exists")
    def search(self,item):
        if(item in self.files):
            print(f"{item} is present inside the directory {self.name}")
        elif(item in self.folders):
            print(f"{item} is present inside the directory {self.name}")
        else:
            for foldername in directory.folders:
                    require_folder = directory.folders[foldername]
                    if item in require_folder.files:
                        print("Item found in ",require_folder)
                    else:
                        print("NOT FOUND")
                        
            
    def __repr__(self):
        return(f"Directory name: {self.name}")
        

def choice(directory,option):
        if(option==1):
                filename = input("Enter file name: ")
                directory.createfile(filename)
        elif(option==2):
                foldername=input("Enter name of folder/sub-directory to be creater: ")
                folder=Directory(foldername)
                directory.createfolder(folder)
        elif(option==3):
                filename=input("Enter file/directory you are searching for:")
                directory.search(filename)
        elif(option==4):
                filename=input("Enter file/directory you want to remove:")
                directory.remove(filename)
        elif(option==5):
                print(f"Directory : {directory.name} - contents ")
                for folder in directory.folders:
                    print(f"(d)-->{folder} ")
                for file in directory.files:
                    print(f"{file} ",end="")
                print("\n")
        elif(option==6):
                foldername=input("Enter the folder you want to open:")
                if(foldername in directory.folders):
                    require_folder = directory.folders[foldername]
                    print(f"Location: {directory.name}/{foldername}\n")
                    for name in require_folder.files:
                        print(f"{name} ")
                        
 
                    
        elif(option==7):
                foldername=input("Enter folder into which you need to add files:")
                filename=input("Enter filename:")
                directory.folders[foldername].createfile(filename)
        elif(option==8):
                print("-----Program Finishes-----")
                exit(0)
        else:
                print("invalid output")
                


name = input("Enter the main directory name: ")
directory  = Directory(name)
print(f"Directory {directory.name} has been created\n")
while(1):
        try:
                print("------------------------------------\n 1.Create File \n 2.Create Folder \n 3.Search \n 4.Remove Folder/File  \n 5.Display  \n 6. Open Folder \n 7.Insert Into\n 8.Exit \n")
                option = int(input("\nEnter Option: "))
                choice(directory,option)
        except:
                print("Error: Exiting Program!")
                break
        
