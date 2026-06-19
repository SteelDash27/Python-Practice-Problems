
students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Carol", 78],
    ["Dave", 92],
    ["Eve", 65]
]


def top_scorers(list):
    highestindex = 0
    highest = 0
    for i in range(0,len(list)):
        if(list[i][1] > highest):
            highest = list[i][1]
            highestindex = i
    print("Top scorer: ",list[highestindex])

def above_average(list):
    sum = 0
    count = 0
    text = "Above average: "
    for i in range(0,len(list)):
        count +=1
        sum += list[i][1]
    average = round(float(sum/count),2)
    print("Average score: ",average)
    for x in range(0,len(list)):
        if(list[x][1] > average):
            text += str(list[x][0]) + " "
    print(text)

"""def reverse_leaderboard(list):
    #temporary variable
    low_to_hi = list

    for i in range(0, len(list)):
        while(i + 1 != len(list)):
            if(low_to_hi[i][1] > low_to_hi[i + 1][1]):
                temp = low_to_hi[i+1][1]
                low_to_hi[i + 1][1] = low_to_hi[i][1]
                low_to_hi[i][1] = temp
    print(low_to_hi)

reverse_leaderboard(students)"""
#top_scorers(students)
#above_average(students)



low = []
for i in range(0,len(students)):
    low.append(students[i][1])

for x in range(0,len(low)):
    if(x != len(low)-1):
        while(low[x] > low[x + 1]):
            temp = low[x+1]
            low[x+1] = low[x]
            low[x] = temp
    else:
        if(low[x-1]>low[x]):
            temp = low[x-1]
            low[x-1] = low[x]
            low[x] = temp

"""if(i+1 != len(low)):
        temp = low[i+1]
        low[i+1] = low[i]
        low[i] = temp
    else:
        if(low[i-1]>low[i]):
            temp = low[i-1]
            low[i-1] = low[i]
            low[i] = temp"""

print(students)
print(low)