
def is_armstrong(num:int):
    #Digits will count the number of digits in the number
    total = 0
    originalnum = num
    digits = len(str(num))
    while(num != 0):
        digit = num % 10
        num //= 10
        total += (digit**digits)

    if(digits == 1):
        return True
    elif(originalnum == total):
        return True
    else:
        return False
    
    

lo = int(input("Enter in the lower range"))
hi = int(input("Enter in the higher range"))

for count in range(lo,hi):
    if (is_armstrong(count) == True):
        print(count)
