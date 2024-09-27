# This code shows how to use string functions

# Convert an integer into a string
new_string = str(123)
print(type(new_string))
print (len(new_string))
print (len("Hello"))


# Concatenate 2 strings 
print ("hello" + "world")

#apply lower method to "Hello"
print ("hello".lower())

#Indexes in Python start from Zero
"Hello"[1]
"Hello"[0:3]

# Use the index string method 
print ("HELLO".index("E"))
print ("HELLO".index("L"))

# Bracket notation refers to the indices placed in square brackets. 
# You can use bracket notation to extract a part of a string. 
device_id = "h32rb17"
print("h32rb17"[0])
print(device_id[0])

#Identifying the length and 
device_id_lenght = len("h32rb17")
if device_id_lenght == 7:
    print ("The device has 7 characters.")
else: 
    print ("all is good")



# Check if the employee id meets length requirements 
 
# Assign `employee_id` to a four digit number as an initial value
employee_id = 4186

# Reassign `employee_id` to the same value but in the form of a string
employee_id = str(employee_id)

# Conditional statement that displays a message if the length of `employee_id` is less than five digits
if len(employee_id) < 5: 
    print("This employee ID has less than five digits. It does not meet length requirements.")


# Assign `employee_id` to a four digit number as an initial value
employee_id = 4186

# Reassign `employee_id` to the same value but in the form of a string
employee_id = str(employee_id)

# Display the `employee_id` as it currently stands
print(employee_id, "is not valid.")

# Conditional statement that updates the `employee_id` if its length is less than 5 digits
if len(employee_id) < 5: 
    employee_id = "E" + employee_id
    
# Display the `employee_id` after the update
print (employee_id)


# Assign `device_id` to a string that contains alphanumeric characters
device_id = "r262c36"

# Extract the fourth character in `device_id` and display it
print(device_id[4])

# Extract the first through the third characters in `device_id` and display the result
print(device_id[0:3])

# Assign `url` to a specific URL
url = "https://exampleURL1.com"

# Extract the protocol of `url` along with the syntax following it, display the result
print (url[0:8])

# Display the index where the domain extension ".com" is located in `url`
print(url.index(".com"))

# Extract the website name in `url` and display it
print (url[8:ind])

# Extract the domain extension in `url` and display it
print(url[ind:ind+4])