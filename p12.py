
x = 10

def outer():
    
    y = 20

    def inner():
        nonlocal y      
        global x        

        z = 30          

      
        y = y + 5
        x = x + 5

        print("Inside inner()")
        print("Local variable z:", z)
        print("Nonlocal variable y:", y)
        print("Global variable x:", x)

    inner()

    print("\nInside outer()")
    print("Nonlocal variable y after modification:", y)


outer()

print("\nIn global scope")
print("Global variable x after modification:", x)
