from heapq import *
# hp is initial head position
# and requests is the list of requests
# no of cylinders is 200
def FCFS(hp,requests):
	time = 0
	n = len(requests)
	pos = hp
	print("\nSequence:")
	print(hp,end='')
	for request in requests:
		time += abs(request-pos)
		pos = request
		print("--->",pos,end='')

	# calculate average seek time
	print("\nTotal seek time:",time)
	avg_seek_time = time / n
	return avg_seek_time
def SCANr(hp,reqs):
	requests = reqs.copy()
	pos = hp
	time = 0
	end=200
	start=0
	print("\nIf head is moving towards 200\n",hp,end='')
	#seek from curr_pos to end which is 200
	for i in range(pos,end+1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print(" ---> ",i,end='')
			requests.remove(i)

	time+=abs(pos-end)-2
	pos=end
	print("----> ",pos-1,end='')
	#seek back to start
	for i in range(end,start-1,-1):
		if i in requests:
			time+=abs(pos-i)
			# print(time)
			pos=i
			print("----> ",i,end='')
			requests.remove(i)
			

	print("\nSeek time :",time)
	# calculate average seek time
	avg_seek_time = time/n
	print("\nAverage Seek Time:",avg_seek_time)

def SCANl(hp,reqs):
        requests=reqs.copy()
        pos=hp
        time=0
        end=199
        start=0
        print("\nIf head is moving towards 0\n",hp,end='')
        #seek from pos to start
        for i in range(pos,start-1,-1):
                if i in requests:
                        time+=abs(pos-i)
                        pos=i
                        print("----> ",i,end='')
                        requests.remove(i)
        time+=abs(pos-start)
        pos=start
        print("----> ",pos,end='')
        #seek back to end
        for i in range(start,end+1):
                if i in requests:
                        time+=abs(pos-i)
                        pos=i
                        print(" ---> ",i,end='')
                        requests.remove(i)
        print("\nSeek time :",time)
        avg_seek_time = time/n
        print("\nAverage Seek Time:",avg_seek_time)
		
def C_SCAN(hp,reqs):
	requests = reqs.copy()
	pos = hp
	time = 0
	end=200
	start=0
	print("\nThe head is always moving towards inwards(to 199)\n",hp,end='')
	#seek from curr_pos to end which is 200
	for i in range(pos,end+1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print("--->",i,end='')
			requests.remove(i)
	time+=abs(pos-end)-2
	print("---> 199 ",end='')
	time+=200
	pos=start
	print("---> 0",end='')
	#seek to hp from start
	for i in range(start,hp+1):
		if i in requests:
			time+=abs(pos-i)
			pos=i
			print("--->",i,end='')
			requests.remove(i)
	
	# calculate average seek time
	print("\nTotal Seek Time:",time)
	avg_seek_time = time/n
	return avg_seek_time

                        

if __name__=='__main__':
	print("DISK SCHEDULING:")
	print("Provide number of I/O requests")
	#n is the number of I/O requests
	n = int(input())
	print("Provide initial position of disc arm (total cylinders=200)")
	hp = int(input())
	while hp>200:
		print("!!! INVALID !!! try again")
		hp = int(input())	
	print("Provide positions to visit : max is 200")
	requests = []
	for i in range(n):
		req = int(input())
		requests.append(req)

	print(requests)
	print("\n")

	print("     --------- FCFS ----------     ")
	print("\nAverage seek time:",FCFS(hp,requests))
	print("  \n   --------- SCAN ----------      ")
	SCANr(hp,requests)
	SCANl(hp,requests)
	print("\n")
	print("     --------- C-SCAN ---------")
	print("\nAvg seek time for  C-scan was ",C_SCAN(hp,requests))
	
	print("\n------------------END-----------------------")
	
