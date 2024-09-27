# This code shows how to use arguments in python

# Explore input and output of print function 

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


# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
def analyze_logins(username, current_day_logins, average_day_logins):

    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)

    # Display a message about average number of login attempts the user has made that day
    print("Average logins per day for", username, "is", average_day_logins)

    # Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`
    login_ratio = current_day_logins/average_day_logins 
    
    # Display a message about the ratio
    print(username, "logged in", login_ratio, "times as much as they do on an average day.")

# Call `analyze_logins()`

analyze_logins("ejones", 9, 3)



# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`

def analyze_logins(username, current_day_logins, average_day_logins):

    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)

    # Display a message about average number of login attempts the user has made that day
    print("Average logins per day for", username, "is", average_day_logins)

    # Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`
    login_ratio = current_day_logins / average_day_logins

    # Return the ratio
    return login_ratio 

# Call `analyze_logins() and store the output in a variable named `login_analysis`

login_analysis = analyze_logins("ejones", 9, 3)

# Display a message about the `login_analysis`
print("ejones", "logged in", login_analysis, "times as much as they do on an average day.")



# Define a function named `analyze_logins()` that takes in three parameters, `username`, `current_day_logins`, and `average_day_logins`
def analyze_logins(username, current_day_logins, average_day_logins):

    # Display a message about how many login attempts the user has made that day
    print("Current day login total for", username, "is", current_day_logins)

    # Display a message about average number of login attempts the user has made that day
    print("Average logins per day for", username, "is", average_day_logins)
    # Calculate the ratio of the logins made on the current day to the logins made on an average day, storing in a variable named `login_ratio`

    login_ratio = current_day_logins / average_day_logins
    # Return the ratio

    return login_ratio

# Call `analyze_logins() and store the output in a variable named `login_analysis`
login_analysis = analyze_logins("ejones", 9, 3)

# Conditional statement that displays an alert about the login activity if it's more than normal
if login_analysis >= 3: 
    print("Alert! This account has more login activity than normal.")