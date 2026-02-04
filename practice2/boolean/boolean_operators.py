x = 5
print(1 < x < 10) #True
print(1 < x and x < 10)#True

bool(5 and 10)      #True
bool(5 and 0)       #False
bool("" and "hi")   #False
bool("hi" and [1])  #True

bool(0 or "")        #False
bool(0 or 5)         #True
bool("hi" or [])     #True
bool([] or {})       #False

bool(not 0)    #True
bool(not 5)    #False
bool(not [])   #True
bool(not [1])  #False

not 0      # True
not 5      # False
not []     # True
not [1]    # False

