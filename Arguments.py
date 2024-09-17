#Explore input and output of print function 
print (type("hello"))
print ("This is a string, but", 75, "is a number.")

#Explore input and output of type 
print (type("security"))
print (type(73.2))

#Max and Min Fucntions 
a = 3 
b = 9 
c = 6
print (max(a, b, c))
print (min(a, b, c))

#Sort the list 
usernames = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "grsparza", "alevitsk", "wjaffery"]
print (sorted(usernames))

# Define a function named `analyze_logins()` that takes in two parameters, `username` and `current_day_logins`
def analyze_logins(username, current_day_logins):

    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)

# Call `analyze_logins()`
analyze_logins("ejones", 9)


# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
def analyze_logins(username, current_day_logins, average_day_logins):

    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)

    # Display a message about average number of login attempts the user has made that day
    print("Average logins per day for", username, "is", average_day_logins)

# Call `analyze_logins()`
analyze_logins("ejones", 9, 4)