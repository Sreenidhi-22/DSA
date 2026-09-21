'''Given an attendance markerwhere 0 represents absent and 1 represents present.Find total number of absentees for the given data
1. No. of.absentees
2.Display with attendance percentage
3.Consider it as a string
'''
'''
attendance = [0,1,1,0,0,1,1,0]
absentees = 0
for i in attendance:
    if i == 0:
        absentees += 1
percentage = ((len(attendance)-absentees)/len(attendance))*100
if absentees > 0:
    print(f"{absentees} student absent out of {len(attendance)}. Att : {percentage:.0f}%")
else:
    print(f"No absentees.Att: {percentage:.0f}%")
'''

attendance = input().split()
absentees = attendance.count('0') 
print (absentees)
percentage = ((len(attendance)-absentees)/len(attendance))*100
if absentees > 0:
    print(f"{absentees} student absent out of {len(attendance)}. Att : {percentage:.0f}%")
else:
    print(f"No absentees.Att: {percentage:.0f}%")

