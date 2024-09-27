# This code shows how to use conditional loops

failed_login = 5
if failed_login > 5:
    print ("Account locked") 
else:
    print ("Login Successful")
  

#create a conditional 
operating_system = "OS 2"
if operating_system == "OS 2": 
    print ("Updates Needed")


#create a conditional 
operating_system = "OS 3"
if operating_system == "OS 2": 
    print ("Updates Needed")
else:
    print ("No Updates Needed")


# Assign `system` to a specific operating system
# This variable represents which operating system is running

system = "OS 3"

# If OS 2 is running, then display a "no update needed" message
# Otherwise if OS 1 is running, display a "update needed" message
# Otherwise if OS 3 is running, display a "update needed" message

if system == "OS 2":
    print("no update needed")
elif system == "OS 1":
    print("update needed")
elif system == "OS 3":
    print ("you have the latest version")
    

# Assign `approved_user1` and `approved_user2` to usernames of approved users
approved_user1 = "elarson"
approved_user2 = "bmoreno"
# Assign `username` to the username of a specific user trying to log in
username = "bmoreno"
# If the user trying to log in is among the approved users, then display a message that they are approved to access this device
# Otherwise, display a message that they do not have access to this device
if username == approved_user1 or username == approved_user2:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")



# Assign `approved_list` to a list of approved usernames
approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
# Assign `username` to the username of a specific user trying to log in
username = "bmoreno"
# If the user trying to log in is among the approved users, then display a message that they are approved to access this device
# Otherwise, display a message that they do not have access to this device
if username in approved_list:
    print ("This user has access to this device.")
elif user not in approved_list: 
    print ("This user does not have access to this device.")


# Assign `organization_hours` to a Boolean value that represents whether the user is trying to log in during organization hours
organization_hours = True
# If the entered `organization_hours` has a value of True, then display "Login attempt made during organization hours."
# Otherwise, display "Login attempt made outside of organization hours."
if organization_hours == True: 
   print ("Login attempt made during organization hours.")
elif organization_hours != True: 
   print ("Login attempt made outside organization hours.")


# Assign `approved_list` to a list of approved usernames
approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]
# Assign `username` to the username of a specific user trying to log in
username = "auehara"
# If the user trying to log in is among the approved users, then display a message that they are approved to access this device
# Otherwise, display a message that they do not have access to this device
if username in approved_list:
    print("This user has access to this device.")
else:
    print("This user does not have access to this device.")
# Assign `organization_hours` to a Boolean value that represents whether the user is trying to log in during organization hours
organization_hours = False
# If the entered `organization_hours` has a value of True, then display "Login attempt made during organization hours."
# Otherwise, display "Login attempt made outside of organization hours."
if organization_hours == True:
    print("Login attempt made during organization hours.")
else:
    print("Login attempt made outside of organization hours.")
    


# Assign `approved_list` to a list of approved usernames
approved_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to the username of a specific user trying to log in
username = "bmoreno"

# Assign `organization_hours` to a Boolean value that represents whether the user is trying to log in during organization hours
organization_hours = True

# If the user is among the approved users and they are logging in during organization hours, then convey that the user is logged in
# Otherwise, convey that either the username is not approved or the login attempt was made outside of organization hours
if username in approved_list and organization_hours == True:
    print("Login attempt made by an approved user during organization hours.")
else:
    print("Username not approved or login attempt made outside of organization hours.")
