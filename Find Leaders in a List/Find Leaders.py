
lst = [16, 17, 4, 3, 5, 2]

def find_leaders(list):
    leaders = []
    for i in range(0,len(list)):#Checks if every
        leader = True
        for x in range(i + 1,len(list)):
            if(list[i] <= list[x]):
                leader = False
                break
        if (leader == True):
            leaders.append(list[i])
    print("Leaders: ",leaders)

find_leaders(lst)
print(lst)