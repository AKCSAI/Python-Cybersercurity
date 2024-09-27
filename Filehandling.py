# This code shows how to read and write to a file 

# The .split() method converts a string into a list.
approved_users = "elarson,bmoreno,tshah,sgilmore,eraab"
print("before .split():", approved_users)
approved_users = approved_users.split(",")
print("after .split():", approved_users)

removed_users = "wjaffrey jsoto abernard jhill awilliam"
print("before .split():", removed_users)
removed_users = removed_users.split()
print("after .split():", removed_users)

#open a text file in python 
with open("/users/azizkhan/python/login_log.txt", 'r') as file: 
        file_text = file.read()
print(file_text.split())

with open("/users/azizkhan/python/login_log.txt", "r") as file:
    updates = file.read()
updates = updates.split()

updates = " ".join(updates)
with open("/users/azizkhan/python/login_log.txt", "w") as file:
    file.write(updates)


# ACTIVITY IMPORT & PARSE A TEXT FILE

# Assign `import_file` to the name of the text file that contains the security log file
import_file = "/users/azizkhan/python/login_log.txt"

# The `with` statement
# Use `open()` to import security log file and store it as a string
with open(import_file, "r") as file:

  # Use `.read()` to read the imported file and store the result in a variable named `text`
  text = file.read()

# Display the contents of `text` split into separate lines 
print(text.split())



# WRITE A MISSING ENTRY TO THE TEST FILE

# Assign `import_file` to the name of the text file that contains the security log file
import_file = "/users/azizkhan/python/login_log.txt"

# Assign `missing entry` to a log that was not recorded in the log file
missing_entry = "jrafael,192.168.243.140,4:56:27,2022-05-09"

# Use `open()` to import security log file and store it as a string
# Pass in "a" as the second parameter to indicate that the file is being opened for appending purposes
with open(import_file, "a") as file:

    # Use `.write()` to append `missing_entry` to the log file
    file.write(missing_entry)

# Use `open()` with the parameter "r" to open the security log file for reading purposes
with open(import_file, "r") as file:

    # Use `.read()` to read in the contents of the log file and store in a variable named `text`
    text = file.read()

# Display the contents of `text`
print(text)


# HOW TO CREATE A BRAND NEW TEXT FILE IN PYTHON

# Assign `import_file` to the name of the text file that you want to create
import_file = "/users/azizkhan/python/new_logfile.txt"

# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"

# Open the file in write mode to create a new file or overwrite an existing file
with open(import_file, 'w') as file:
    # Write `ip_addresses` to the file
    file.write(ip_addresses)

# Display `import_file`
print("File created:", import_file)

# Display `ip_addresses`
print(ip_addresses)


# Assign `import_file` to the name of the text file that you want to create

import_file = "/users/azizkhan/python/allow_list.txt"

# Assign `ip_addresses` to a list of IP addresses that are allowed to access the restricted information
ip_addresses = "192.168.218.160 192.168.97.225 192.168.145.158 192.168.108.13 192.168.60.153 192.168.96.200 192.168.247.153 192.168.3.252 192.168.116.187 192.168.15.110 192.168.39.246"

# Create a `with` statement to write to the text file 
with open(import_file, "w") as file:

    # Write `ip_addresses` to the text file
    file.write(ip_addresses)

# Create a `with` statement to read in the text file 
with open(import_file, "r") as file: 

    # Read the file and store the result in a variable named `text`
    text = file.read()

# Display the contents of `text`
print(text)



