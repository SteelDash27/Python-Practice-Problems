
lst = [5,5,5,5]

def two_sum(list, target: int):
    ListIndexPair = []
    for i in range(0,len(list)):
        for x in range(i+1,len(list)):
            if((list[i] + list[x]) == target):
                print([i,x])
                ListIndexPair.append([i,x])
    print(ListIndexPair)

two_sum(lst,10)
                