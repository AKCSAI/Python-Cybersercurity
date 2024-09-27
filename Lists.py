# This code shows how to use lists

# Extract from a list
my_list = ["a", "b", "c", "d", "e"]
print(my_list[1])

# List Concatenation (Combining Lists)
my_list = ["a", "b", "c", "d", "e"]
number_list = [1, 2, 3, 4]
print (my_list + number_list)

# Change an element in the list 
my_list = ["a", "b", "c", "d", "e"]
my_list [1] = 7 
print (my_list)

# Use the insert method
my_list = ["a", "b", "c", "d", "e"]
my_list.insert (1,7)
print (my_list)

# Remove the element from the list 
my_list = ["a", "b", "c", "d", "e"]
my_list.remove ("d")
print (my_list)


# extract the first three characters of an IP address
# Parsing IP Addresses
address = "198.223.xx.xx"
print (address [0:3])

#Using Index fucntion to extract list where the occurance resides in the list 
username_list = ["bmoreno", "wjaffrey", "tshah", "sgilmore", "btang"]
username_index = username_list.index("tshah")
print(username_index)


# Using append function to add a name to the list 
username_list = ["bmoreno", "wjaffrey", "tshah", "sgilmore"]
print("Before appending an element:", username_list)
username_list.append("btang")
print("After appending an element:", username_list)


# Extract the first three characters from a list of IP addresses
IP = ["198.223.xx.xx", "198.101.xx.xx", "180.064.xx.xx", "192.168.xx.xx", "184.090.xx.xx"]
networks = []
for address in IP: 
    networks.append (address[0:3])
print (networks)


# Adding numbers to an emply list 
numbers_list = []
print("Before appending a sequence of numbers:", numbers_list)
for i in range(10):
    numbers_list.append(i)
print("After appending a sequence of numbers:", numbers_list)


# Add new users and devices to existing lists. 

# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir"]

# Assign `new_user` to the username of a new approved user
new_user = "gesparza"

# Assign `new_device` to the device ID of the new approved user
new_device = "3rcv4w6"

# Add that user's username and device ID to `approved_users` and `approved_devices` respectively
approved_users.append(new_user)
approved_devices.append(new_device)

# Display the contents of `approved_users`
print (approved_users)

# Diplay the contents of `approved_devices`
print (approved_devices)



# Remove users from the list 

# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "2ye3lzg", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `removed_user` to the username of the employee who has left the team
removed_user = "tshah"

# Assign `removed_device` to the device ID of the employee who has left the team
removed_device = "2ye3lzg"

# Remove that employee's username and device ID from `approved_users` and `approved_devices` respectively
approved_users.remove(removed_user)
approved_devices.remove(removed_device)

# Display the contents of `approved_users`
print (approved_users)

# Diplay the contents of `approved_devices`
print (approved_devices)




# Find an index in one list and then use this index to display connected information in another list.

# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username
username = "sgilmore"

# Conditional statement
# If `username` belongs to `approved_users`, then display "The user ______ is approved to access the system."
# Otherwise display "The user ______ is not approved to access the system."
if username in approved_users: 
    print("The username", username, "is approved to access the system.")
else: 
    print("The username", username, "is approved to access the system.")




# Write a conditional that checks if the username is an element of the approved_devices and if the device_id

# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username
username = "sgilmore"

# Assign `device_id` to a device ID
device_id = "4n482ts"

# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)

# Conditional statement
# If `username` belongs to `approved_users`, and if the device ID at `ind` in `approved_devices` matches `device_id`,
# then display a message that the username is approved,
# followed by a message that the user has the correct device

if username in approved_users and approved_devices: 
    print("The username", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)



#Add to the code by writing an elif statement. 
# This elif statement should run when the username is part of the approved_users 
# but the device_id doesn't match the corresponding device ID in the approved_devices. 

# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Assign `username` to a username
username = "sgilmore"

# Assign `device_id` to a device ID
device_id = "4n482ts"

# Assign `ind` to the index of `username` in `approved_users`
ind = approved_users.index(username)

# If statement
# If `username` belongs to `approved_users`, and if the element at `ind` in `approved_devices` matches `device_id`,
# then display a message that the username is approved,
# followed by a message that the user has the correct device

if username in approved_users and device_id == approved_devices[ind]:
    print("The user", username, "is approved to access the system.")
    print(device_id, "is the assigned device for", username)

# Elif statement
# Handles the case when `username` belongs to `approved_users` but element at `ind` in `approved_devices` does not match `device_id`,
# and displays two messages accordingly

elif username in approved_users != approved_devices[ind]: 
    print("The user", username, "is approved to access the system, but", device_id, "is not their assigned device.")



# Complete your algorithm by developing a function that uses some of the code you've written in earlier tasks

# Assign `approved_users` to a list of approved usernames
approved_users = ["elarson", "bmoreno", "sgilmore", "eraab", "gesparza"]

# Assign `approved_devices` to a list of device IDs that correspond to the usernames in `approved_users`
approved_devices = ["8rp2k75", "hl0s5o1", "4n482ts", "a307vir", "3rcv4w6"]

# Define a function named `login` that takes in two parameters, `username` and `device_id`
def login(username, device_id): 

    # If `username` belongs to `approved_users`,

    if username in approved_users:

        # then display "The user ______ is approved to access the system.",

        print("The user", username, "is approved to access the system.")

        # assign `ind` to the index of `username` in `approved_users`,

        ind = approved_users.index(username)

        # and execute the following conditional
        # If `device_id` matches the element at the index `ind` in `approved_devices`,

        if device_id == approved_devices[ind]:

          # then display "______ is the assigned device for ______"

          print(device_id, "is the assigned device for", username)

        # Otherwise,

        else:

          # display "______ is not their assigned device"

          print(device_id, "is not their assigned device.")

    # Otherwise (part of the outer conditional and handles the case when `username` does not belong to `approved_users`),

    else:

        # Display "The user ______ is not approved to access the system."

        print("The username", username, "is not approved to access the system.")

# Call the function you just defined to experiment with different username and device_id combinations

login("elarson", "8rp2k75")
login("bmoreno", "hl0s5o1")
