# creatung a class and variable
# here this is equal to self
# constructor = init
# polymorphism can be done fro parameter also like different execution for diffrent data type
# staticm functions are those which are accessible by class but not instance of the class

# dude another thing is that every function must contain self in order to called by obj

# decorator are nothing but guardrail impost on function like the obj must satidfy certain conditions to call this function etc

# here we are creating a method which can be used by only class not obj of that class

class Car:
    totalObjCreated = 0

    def __init__(self,brand,model):
        self.__brand = brand #now brand is a private variable
        self.__model = model
        Car.totalObjCreated += 1 #even this will get plus one for child class object also

    def full(self):
      return  print(self.__brand) #here the thing is you have to give self explicitly in the parameter
    
    def get_brand(self): #you can give any function name you like but this coems under good practice
      return  print(self.__brand)
    
    @staticmethod
    def onlyClassMethod(): #no self is req since no obj
       print("Iam the class calling not object")

    # lets make a property only readable but not writable
    @property
    def model(self):
       return self.__model

obj1 = Car("BMW","kk")
# obj1.model="kkkkkk"   #you cant do this since the variable is readOnly now
print("Model: ",obj1.model) #carefull u can access this as a variable
# print(obj1.brand)
print(obj1.full()) #you will none since its not returning anything that print statement gets executed earlier
        

#inheritance
class ElectricCar(Car):
    def __init__(self, brand, model):
      super().__init__(brand, model) # we are calling the constructor of the parent class
    
    def full(self):
      print(self.brand,"jhdhdh")

car2= ElectricCar("vv","kk")
# print(car2.full())
print(isinstance(car2,Car))
print(isinstance(car2,ElectricCar))


print(Car.totalObjCreated)
print(Car.onlyClassMethod())

# class A:
#     x = 1

# class B:
#     x = 2

# class C(A, B):
#     pass

# print(C.x)  # Output: 1 multiple inheritance example the first class gets the preference
