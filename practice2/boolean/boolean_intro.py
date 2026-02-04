
print(bool("Hello")) #True
print(bool(15))      #True
print(bool(""))      #False
print(bool(0))       #False
print(bool([0]))     #True

#The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool('')
bool(())
bool([])
bool({})

print(bool(1))     #True
print(bool(0))     #False

bool(0.0)       # False
bool(set())     # False 
bool((0,))      # True




