import sys 
def square(num):
    squared = num * num 
    return squared 
a = int (input("enter a number:"))
a = int(sys.argv[1])
b = square(a)
print("square of ",a,"is",b)