currently_allocated=[]
max_need=[]
const_avail=[]
safe_st=[0]*5
def main():
  
        processes = int(input("How many processes are requesting resources?  "))
        resources = int(input("Number of resources availabe?: "))
        max_resources = list(map(int,input("Enter maximum available instances of each resource: ").split()))
        print("\nEnter number of allocated resources for each process ")
        for j in range(processes):
            eachp=list(map(int,input(f'process {j + 1} :').split()))
            currently_allocated.append(eachp)
     

        print("\n--Enter the number of maximum resources for each process --")
        for j in range(processes):
            eachmax=list(map(int,input(f'process {j + 1} :').split()))
            max_need.append(eachmax)
        

        allocated = [0] * resources
        for i in range(processes):
            for j in range(resources):
                allocated[j] += currently_allocated[i][j]
        print(f"\ntotal allocated resources : {allocated}")

        available = [max_resources[i] - allocated[i] for i in range(resources)]
        print(f"total available resources : {available}\n")
        const_avail=available
        running = [True] * processes
        count = processes
        while count != 0:
            safe = False
            for i in range(processes):
                if running[i]:
                    executing = True
                    for j in range(resources):
                        if max_need[i][j] - currently_allocated[i][j] > available[j]:
                            executing = False
                            break
                    if executing:
                        safe_st.append(i+1)
                        print(f"process {i + 1} is executing")
                        running[i] = False
                        count -= 1
                        safe = True
                        for j in range(resources):
                            available[j] += currently_allocated[i][j]
                        break
            if not safe:
                print("the processes are in an unsafe state.")
                break

            print(f"the process is in a safe state.\navailable resources : {available}\n")
if __name__ == '__main__':
    main()
    print("Safe Sequence:",safe_st[5:])

