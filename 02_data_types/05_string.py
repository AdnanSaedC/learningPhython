# >>> """\n adnan\n"""
# '\n adnan\n' this preserves everything

# variable[starting index: index you want to end +1:hop]
# >>> num='0123456789'
# >>> num[::2]
# '02468'

# >>> num = 'adnan'
# >>> num.lower()
# 'adnan'
# >>> num.upper()
# 'ADNAN'

# >>> space = ' gggg '
# >>> space.strip() it removes the spaces that's it
# 'gggg'
# >>> space
# ' gggg '
# >>> 

# >>> var = 'lemon tea'
# >>> var
# 'lemon tea'
# >>> var.replace('lemon','ginger')
# 'ginger tea'
# >>> var
# 'lemon tea'  u still got lemon tea because strings are immutable

# string 
string = 'lemon ginger'
print(string.split()) #now it will convert this string into list
# ['lemon', 'ginger']

# >>> var = 'adnan saed'
# >>> var.find('saed')
# 6 if not found then -1

# var.count('string')

# >>> item = 'burger'
# >>> quan = 2

# >>> order = 'I ordered {} {}'
# >>> order.format(quan,item)
# 'I ordered 2 burger'

# list to string
# >>> list=['1','2']
# >>> print(" ".join(list))  to convert list to string
# 1 2
# >>>
# 
# >>> var = " ccc\" "
# >>> var
# ' ccc" ' to store double quotes
# >>>  

# >>> var = r"hhhh \n jhjhjk" to store raw store string
# >>> var
# 'hhhh \\n jhjhjk'
# >>> 

# >>> var = 'adnan saed'
# >>> 'adnan' in var  to check whether a piece exist or not
# True