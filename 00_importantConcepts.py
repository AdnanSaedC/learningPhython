score = 0

if score>100:
    exit()
elif score>50:
    print("djdjdj")
else:
    score = "your score is " + str(score)
    print(score)


# reversing a string
str = "python"
reversed_str =""

for char in str:
    reversed_str = char+reversed_str  #p->yp->typ ...
print(reversed_str)

# if you add break then it will break out of all loops

list =[1,2,3,5,1,6]
print(set(list)) #you will get an output and set with only one 1