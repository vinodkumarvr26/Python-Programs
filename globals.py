def show():
    y = 20 
    global x
    print("Inside function  x =", x)
    print("Inside function y =", y)
    x=x+5
    print("after updating global Inside function  x =", x)
show()
print("Outside function x =", x)
