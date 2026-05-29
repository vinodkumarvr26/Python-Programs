x = 10 
def show():
    x = 20   # local variable with same name
    print("Local x inside function =", x)
    print("Global x inside function =", globals()['x'])
show()
print("global variable outside function x =", x)
