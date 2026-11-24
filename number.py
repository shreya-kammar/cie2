import sys 
def square(num):
    squared = num * num 
    return squared 
if __name__ == "__main__":
   a = int(sys.argv[1])
   a =  input("enter a number:")

   b = square(a)
   print("square of ",a,"is",b)   