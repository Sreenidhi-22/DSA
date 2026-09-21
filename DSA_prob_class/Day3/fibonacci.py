'''Find fibonacci and it's time and space complexity'''
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
try:
    n = int(input())
    fibonacci(n)
except Exception as e:
    print("Provid valid input")
#Time complexity: O(n)
#Space complexity: O(1)
    
    