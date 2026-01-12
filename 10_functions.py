def square(num=16):
    print(num**2)
    return num,None #it will return a tuple 

# print(square(4))

def just():
    pass

# lamda function or anonimous function
cube = lambda parameter:parameter**3
another = cube

# the number of argument is not constant
def sumAll(*args): #ansterik is the one which help us to get any number of argument we want
    print("just arguments: ",args)
    print("with *: ",*args)
    return args,*args
    # *args gives value as such were as args gives a tuple


# print(cube(6))
# print(another(6))
# print(sumAll(1,3,5))
# print(sumAll(1,8,5))


# named arguments
# keyWord Argument
def keyValue(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    print("\n")

# keyValue(name="adnan")
# keyValue(name="adnan",c="uni")
# keyValue(name="adnan",c="uni",d="l")


# yield
# range(start,limit(last value not inclusive),step+1(this if step is 2 it will skip 1,similarly for 3 it will skip 2))

# the thing is we want to return one by one value from a list using a function
# how to do that 
# the goal it return something and at the same time keep track of memory

def evenGeneratot(num):
    for i in range(2,num+1,2):
        # return i what it will do is it will return 2 and finish
        # this will return 2 and at the same time keep the funcion running till last value
        yield i

for i in evenGeneratot(10):
    print(i)

# while designing recursive functions focus on exit part
