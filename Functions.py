# This code shows how to use function

#Define a function 
def greet_employee():
    print ("Welcome. You are logged in.")

#call a function 
greet_employee()


# Define a function named `list_to_string()`
def list_to_string():
  # Store the list of approved usernames in a variable named `username_list`
  username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]

  # Write a for loop that iterates through the elements of `username_list` and displays each element
  for i in username_list:
    print(i)

# Call the `list_to_string()` function
list_to_string()


# Define a function named `list_to_string()` - Concatenation Example

def list_to_string():

  # Store the list of approved usernames in a variable named `username_list`

  username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]

  # Assign `sum_variable` to an empty string

  sum_variable = ""

  # Write a for loop that iterates through the elements of `username_list` and displays each element

  for i in username_list:
    sum_variable = sum_variable + i 

  # Display the value of `sum_variable`
    print (sum_variable)

# Call the `list_to_string()` function

list_to_string()


# Define a function named `list_to_string()`

def list_to_string():

  # Store the list of approved usernames in a variable named `username_list`
  username_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab", "gesparza", "alevitsk", "wjaffrey"]
  
  # Assign `sum_variable` to an empty string
  sum_variable = ""
  
  # Write a for loop that iterates through the elements of `username_list` and displays each element
  for i in username_list:
    sum_variable = sum_variable + i + ", "

  # Display the value of `sum_variable`
  print(sum_variable)

# Call the `list_to_string()` function
list_to_string()


