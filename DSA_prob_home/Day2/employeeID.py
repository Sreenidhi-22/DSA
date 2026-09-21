'''Given n employee IDs determine wether all IDs are unique;
print YES if every ID occurs once else NO.

Constrains:
- Input will be numeric
'''
employeeID = input().split()
unique = 0
for i in employeeID:
    if employeeID.count(i) > 1:
        unique += 1
if unique > 1:
    print("NO")
else:
    print("YES")