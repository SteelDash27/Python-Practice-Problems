
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

def reverse_leaderboard(list):
    #temporary variable
    low_to_hi = list
    temp = 0

    for i in range(0, len(list)):
        while(i + 1 != len(list)):
            if(low_to_hi[i][1] > low_to_hi[i + 1][1]):
                temp = low_to_hi[i+1][1]
                low_to_hi[i + 1][1] = low_to_hi[i][1]
                low_to_hi[i][1] = temp
    print(low_to_hi)

reverse_leaderboard(students)
#top_scorers(students)
#above_average(students)