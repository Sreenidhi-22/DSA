''' To find the average of odd and even numbers in an array. Output - round off to 2 decimals '''
arr = [10,2,19,27,16,3]
even = []
odd = []
for i in arr:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
if len(even) == 0:
    print("Even Average:0.00")
else:
    even_avg = sum(even)/len(even)
    print(f"Even Average: {even_avg:.2f}")
if len(odd) == 0:
    print("Odd Average:0.00")
else:
    odd_avg = sum(odd)/len(odd)
    print(f"Odd Average: {odd_avg:.2f}")
