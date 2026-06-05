
#n: int
def times_table():
    count = 1, times = 1
    num = int(input("Enter in a number"))

    while(times <= num): 
        for x in range(count*times, num+1):
            print(count*times, end = " ")
            if((count % num) == 0):
                print()
            count= count +1
        print()
       
times_table()