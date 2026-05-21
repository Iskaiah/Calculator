def add (x, y): return x + y
def subtract(x, y): return x-y
def multiply(x, y): return x * y
def divide(x, y): 
    if y != 0:
        return x / y

def calculator():
    print("Select Operation: +, -, / or 'q' to quit")
    while True:
        choice = input("Operation: ")
        if choice == 'q': break
        try:
            n1 = float(input("Num 1: "))
        
        except ValueError: Print("Invalid number")

if __name__ == "_main_": calculator()