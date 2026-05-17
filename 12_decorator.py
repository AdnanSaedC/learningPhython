import time

def timer(func): #this is to get the function
    def wrapper(*args,**kwargs): #first is to get the unnamed para and the next is named para
        start = time.time()
        result = func(*args,**kwargs) #here we are executing the funtion
        end = time.time()
        print(f"{func.__name__} executed {end-start}")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)

# timer(example_function(5))
# def timer(func): #this is to get the function
#     def wrapper(*args,**kwargs): #first is to get the unnamed para and the next is named para
#         start = time.time()
#         result = example_function(n) #here we are executing the funtion
#         end = time.time()
#         print(f"{func.__name__} executed {end-start}")
#         return result
#     return wrapper
# # when we call this we get a wrapper and the value goes from thta

example_function(5)
