import sys 
def square(num):
    squared = num * num 
    return squared 
a = int(sys.argv[1])
a = int (input("enter a number:"))

b = square(a)
print("square of ",a,"is",b)