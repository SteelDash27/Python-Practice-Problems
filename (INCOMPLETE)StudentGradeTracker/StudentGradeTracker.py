
numStudents = int(input("Enter in the number of students: "))
scores = []
    
count = 1
for i in range(0,numStudents):
    scores.append(int(input(f"Enter score for student {i+1}: ")))
    if(scores[i] > (sum(scores)/len(scores))):
        count +=1

print(scores)

def maximum(lis: int):
    for i in range():
        




print("Highest mark: ",max(scores))
print("Lowest mark: ",min(scores))
print("Average mark: ",float(sum(scores)/len(scores)))
print("Number of marks above the average")