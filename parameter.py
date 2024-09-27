# This code shows how to use parameters

#Greet employees by name 
def greet_employees(name):
    print ("Welcome! You're logged in", name)

greet_employees("Charlie Patel")


#Greet employee by first name and last name
def greet_employee(first_name, last_name): 
    print ("Welcome, You're logged in!", first_name, last_name)

greet_employee ("William", "Wallace")



#Return information from a function 
def calculate_fails(total_attempts, failed_attempts):
    fail_percentage = failed_attempts / total_attempts
    return fail_percentage

percentage = calculate_fails(4,2)

if (percentage >= .5):
    print ("Account Locked.")

