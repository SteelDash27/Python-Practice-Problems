
lst = [1,2,3,4,5]

def rotate_list(list, k: int):
    for i in range(0,k):#Moves numbers to the right once
        LastDigit = list[len(list) - 1]
        for x in range(len(list) - 1, 0, -1):#moves every number to the right
            list[x] = list[x - 1]
        list[0] = LastDigit

rotate_list(lst,2)
print(lst)       