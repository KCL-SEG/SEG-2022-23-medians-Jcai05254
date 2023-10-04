"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
def chooseMedian(numbers):
    numbers.sort()
    
    n = len(numbers)
    
    if n%2 == 1:
        median = numbers[n//2]
        
    elif n%2 == 0:
        middle1 = numbers[n//2 -1]
        middle2 = numbers[n//2 ]
        median = (middle1 + middle2)/2
        
    return median
    
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)
print(chooseMedian(numbers))