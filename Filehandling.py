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
with open("/users/azizkhan/downloads/transcript.txt", 'r') as file: 
        file_text = file.read()
print(file_text.split())

with open("/users/azizkhan/downloads/transcript.txt", "r") as file:
    updates = file.read()
updates = updates.split()

updates = " ".join(updates)
with open("/users/azizkhan/downloads/transcript.txt", "w") as file:
    file.write(updates)