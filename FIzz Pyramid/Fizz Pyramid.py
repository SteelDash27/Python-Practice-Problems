

def fizz_pyramid(n: int):
    for row in range(1,n+1):
        for col in range(1,row+1):
            #print(col, end = " ")
            if(((col % 3) == 0) and ((col % 5) == 0)):
                print("FizzBuzz", end = " ")
            elif((col % 3) == 0):
                print("Fizz", end = " ")
            elif((col % 5) == 0):
                print("Buzz",end = " " )
            else:
                print(col, end = " ")
        print()


rows = 20
fizz_pyramid(rows)

