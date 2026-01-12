# higher order function which is nothing but it takes a function as an argument
import time

def timer(func): #this is to get the function
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__} executed {end-start}")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

# timer(example_function(5))
# when we call this we get a wrapper and the value goes from thta

example_function(5)