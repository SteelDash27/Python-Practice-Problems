
numStudents = int(input("Enter in the number of students: "))
scores = []

def maximum(lst):
    maxnum = 0
    for x in range(0,len(lst)):
        if(lst[x] > maxnum):
            maxnum = lst[x]
    print("Highest mark: ", maxnum)

def minimum(lst):
    minnum = 100
    for i in range(0, len(lst)):
        if(lst[i] < minnum):
            minnum = lst[i]
    print("Lowest mark: ",minnum)

def average(lst):
    count = 0
    sum = 0
    for z in range(0,len(lst)):
        sum += lst[z]
        count +=1
    return round(float(sum/count),2)
    #print("Average mark: ",round(sum/count,2))


def report_scores(lst):
    count = 0
    for i in range(0,numStudents):
        scores.append(int(input(f"Enter score for student {i+1}: ")))
        if(scores[i] > average(lst)):
            count +=1
    if(count == 0):
        count = " "

    print("\nMarks: ",scores, "\n")
    maximum(lst)
    minimum(lst)
    average(lst)
    print("Number of marks above the average: ", count,"\n")


report_scores(scores)