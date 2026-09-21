'''Write a program to find 1st and 2nd largest element '''

arr = [10,29,9,47,26]
first_largest = 0
second_largest = 0
for i in arr:
    if first_largest < i:
        second_largest = first_largest
        first_largest = i
print(f"First largest = {first_largest}")
print(f"Second largest = {second_largest}")
