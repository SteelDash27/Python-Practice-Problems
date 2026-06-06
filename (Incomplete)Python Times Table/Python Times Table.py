      
def times_table():
    row = 1
    times = 1
    num = int(input("Enter in a number: "))
    widthmax = len((str)(num*num))

    for i in range(row,num+1):#outer for loop
        for j in range(1,num+1):
            #print(j*times, end = " ")
            if(j < 10):
                print((str)(j*times).rjust(widthmax),end= " ")
            else:
                print(j*times, end= "")
        times = times + 1
        print()

times_table()
