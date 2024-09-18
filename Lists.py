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


# Extract the first three characters from a list of IP addresses
IP = ["198.223.xx.xx", "198.101.xx.xx", "180.064.xx.xx", "192.168.xx.xx", "184.090.xx.xx"]
networks = []
for address in IP: 
    networks.append (address[0:3])
print (networks)
