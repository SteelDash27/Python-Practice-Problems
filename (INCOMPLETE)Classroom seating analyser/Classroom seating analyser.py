
classroom = [
    [85, 90, 78, 92, 88],
    [70, 65, 80, 75, 95],
    [55, 60, 72, 68, 58],
    [91, 84, 77, 89, 93]
]

def top_students(lst,threshold):
    above = [] #list of scors above threshold
    for row in range(0,len(classroom)):#Takes the number of rows
        for position in lst[row]:
            if(position > threshold):
                above.append(position)
    print(f"Top scores (above {threshold}): ",above)

def row_averages(lst):
    average = []
    for row in range(0,len(lst)):
        count = 0
        sum = 0
        for num in lst[row]:
            count += 1
            sum += num
            average.append(round(float(sum/count)),2)
        
    print(average)


"""threshold = int(input("Enter in a number that acts as the threshold"))
top_students(classroom , 80)"""
row_averages(classroom)
   