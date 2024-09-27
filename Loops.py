#This code shows how to use loops

y = [1, 2, 3, 4, 5, 6, 7, 8]
for i in y: 
    print (i) 


#run for loop with range 
for i in range(10): 
    print ("Cannot connect to the destination")

#run a while loop with increment of 1 
time = 0 
while time <= 10: 
    print (time)
    time = time + 1 

#create a while loop for maximum devices 
max_device = 5 
i = 1 
while i < max_device: 
    print ("User can still connect with additonal devices")
    i = i + 1
print ("The user has reached max number of devices")

#print items in a table 
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    print(asset)

#Login Attempts Count
login_attempts = 0
while login_attempts < 5:
    print("Login attempts:", login_attempts)
    login_attempts = login_attempts + 1

#login status    
count = 0
login_status = True
while login_status == True:
    print("Try again.")
    count = count + 1
    if count == 4:
        login_status = False    


#Break is used to exit a loop if certain condition is met
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        break
    print(asset)#using break statement 


#Continue is used to enter the loop is certain condition is met 
computer_assets = ["laptop1", "desktop20", "smartphone03"]
for asset in computer_assets:
    if asset == "desktop20":
        continue
    print(asset)


# Assign `allow_list` to a list of IP addresses that are allowed to log in

allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”

for i in ip_addresses: 
	if i in allow_list:
		print ("IP address is allowed")
	else:
		print ("IP address is not allowed")
          

 # Assign `allow_list` to a list of IP addresses that are allowed to log in

allow_list = ["192.168.243.140", "192.168.205.12", "192.168.151.162", "192.168.178.71", 
              "192.168.86.232", "192.168.3.24", "192.168.170.243", "192.168.119.173"]

# Assign `ip_addresses` to a list of IP addresses from which users have tried to log in

ip_addresses = ["192.168.142.245", "192.168.109.50", "192.168.86.232", "192.168.131.147",
                "192.168.205.12", "192.168.200.48"]

# For each IP address in the list of IP addresses from which users have tried to log in, 
# If it is among the allowed addresses, then display “IP address is allowed”
# Otherwise, display “IP address is not allowed”
               
for i in ip_addresses: 
	if i in allow_list:
		print ("This IP address is allowed.", ip_addresses)
	else:
		print ("This IP address is not allowed. Further investigation of login activity required.")
		break         
     

# Assign the loop variable `i` to an initial value of 5000

i = 5000

# While loop that generates unique employee IDs for the Sales department by iterating through numbers
# and displays each ID created

while i <= 5150:
    print (i)
    i = i + 5     

# Assign the loop variable `i` to an initial value of 5000

i = 5000

# While loop that generates unique employee IDs for the Sales department by iterating through numbers
# and displays each ID created
# This loop displays "Only 10 valid employee ids remaining" once `i` reaches 5100

while i <= 5150: 
    print(i)
    if i == 5100:
        print ("Only 10 valid employee ids remaining.")
    i = i + 5    

