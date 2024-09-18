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