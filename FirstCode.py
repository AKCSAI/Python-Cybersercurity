#Print Hello 
print ("hello python")
print("I am using Python.")
print("I am a security analyst.")
print("Python is useful for security!")
print (1+2) 
print (10<5)
print (11>10)
# Print a list
print (["a", "b", "c"])
# Use a variable to store a device id 
device_id = "hr1234"
print (device_id)
print ("m40pi31")
#Use the type function 
device_id = "hr1234"
data_type = type (device_id)
print(data_type)

#reassign a variable 
device_id = "hr1234"
print (device_id)
device_id = "sa4321"
print (device_id)

username = "asamiu"
old_username = username 
username = "azizk"
print ("Previous username:", old_username)
print ("New Username:", username)

# Assign `username_list` to the list of usernames who are allowed to access the device
username_list = ["madebowa", "jnguyen", "tbecker", "nhersh", "redwards"]
# Assign `username_list_type` to the data type of `username_list`
username_list_type = type (username_list)
# Display `username_list_type`
print (username_list ,username_list_type)

# Assign `max_logins` to the value 3
max_logins = 3
# Assign `max_logins_type` to the data type of `max_logins`
max_logins_type = type(max_logins)
# Display `max_logins_type`
print (max_logins_type)

# Assign `max_logins` to the value 3
max_logins = 3
# Assign `login_attempts` to the value 2
login_attempts = 2
# Determine whether the current number of 
# login attempts a user has made is less than or equal to the 
# maximum number of login attempts allowed,
# and display the resulting Boolean value
print(login_attempts <= max_logins)

# Assign `login_status` to the Boolean value False
login_status = "False"
# Assign `login_status_type` to the data type of `login_status`
login_status_type = type(login_status)
# Display `login_status_type`
print(login_status_type)

