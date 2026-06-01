
#n: int
def times_table():
    count = 1
    num = int(input("Enter in a number"))

    times = 1
    for i in range(times,num): 
        for x in range(count, num+1):
            print(count * times, end = " ")
            if((count % num) == 0):
                print()
            count= count +1
        print()
        times += 1
       
times_table()