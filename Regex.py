# Email addresses 
import re
email_log = "mazizk08@gmail.com"
print(re.findall ("\w+@\w+\.\w+", email_log))

# Running Regex - Findall in One Line
import re
re.findall ("ts", "tsnow, tshah, bmoreno") #"\ts" finds only ts in the string
re.findall("\w", "h32rb17") #\w finds all characters
re.findall("\d", "h32rb17") #\d finds all single digits [0-9]
re.findall("\d+", "h32rb17") #\d+ finds numbers 
re.findall("\d*","h32rb17") #\d* skips all alphabets and shows numbers
re.findall("\s","h32rb17") #\s matches to all single spaces 

#\d{2} instructs Python to return all matches of exactly two single digits in a row
re.findall("\d{2}", "h32rb17 k825t0m c2994eh")

#\d{1,3} asks python to display index 1-3
re.findall("\d{1,3}", "h32rb17 k825t0m c2994eh")

# Finding items with specific symbols \w+, :, \s, and \d+ 
pattern = "\w+:\s\d+"
employee_logins_string = "1001 bmoreno: 12 Marketing 1002 tshah: 7 Human Resources 1003 sgilmore: 5 Finance"
print(re.findall(pattern, employee_logins_string))



# Find Patterns In The Log 

# Assign `devices` to a string containing device IDs, each device ID represented by alphanumeric characters
devices = "r262c36 67bv8fy 41j1u2e r151dm4 1270t3o 42dr56i r15xk9h 2j33krk 253be78 ac742a1 r15u9q5 zh86b2l ii286fq 9x482kt 6oa6m6u x3463ac i4l56nq g07h55q 081qc9t r159r1u"

# Assign `target_pattern` to a regular expression pattern for finding device IDs that start with "r15"
target_pattern = "r15\w+"

# Use `re.findall()` to find the device IDs that start with "r15" and display the results
print(re.findall(target_pattern, devices))


# FINDING IP ADDRESSES ONLY IN A LOG USING FINDALL FUNCTION 

# Assign `log_file` to a string containing login information with potential invalid IP addresses
log_file = """eraab 2022-05-10 6:03:41 192.168.152.148 
iuduike 2022-05-09 6:46:40 192.168.22.115 
smartell 2022-05-09 19:30:32 192.168.190.178 
arutley 2022-05-12 17:00:59 1923.1689.3.24 
rjensen 2022-05-11 0:59:26 192.168.213.128 
aestrada 2022-05-09 19:28:12 1924.1680.27.57 
asundara 2022-05-11 18:38:07 192.168.96.200 
dkot 2022-05-12 10:52:00 1921.168.1283.75 
abernard 2022-05-12 23:38:46 19245.168.2345.49 
cjackson 2022-05-12 19:36:42 192.168.247.153 
jclark 2022-05-10 10:48:02 192.168.174.117 
alevitsk 2022-05-08 12:09:10 192.16874.1390.176 
jrafael 2022-05-10 22:40:01 192.168.148.115 
yappiah 2022-05-12 10:37:22 192.168.103.10654 
daquino 2022-05-08 7:02:35 192.168.168.144"""

#BASIC WAY OF FINDING THE IP ADDRESSES 

# Assign `pattern` to a regular expression pattern that will match with IP addresses of the form xxx.xxx.xxx.xxx
pattern = "\d\d\d.\d\d\d.\d\d\d.\d\d\d"
pattern = "\d+\.\d+\.\d+\.\d+" #performs the same function as above
pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" #using pattern matching

# Use the `re.findall()` function on `pattern` and `log_file` to extract the IP addresses
print (re.findall(pattern, log_file))

#ADVANCED WAY - USING \B FOR BOUNDRY AND \D{X,X} FOR RANGE 

# Improved pattern to match valid IP addresses (of the form xxx.xxx.xxx.xxx)
pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

# Output the matches
print(re.findall(pattern, log_file))

# FINDING FLAGGED IP ADDRESSES 
# Assign `log_file` to a string containing username, date, login time, and IP address for a series of login attempts 
log_file = "eraab 2022-05-10 6:03:41 192.168.152.148 \niuduike 2022-05-09 6:46:40 192.168.22.115 \nsmartell 2022-05-09 19:30:32 192.168.190.178 \narutley 2022-05-12 17:00:59 1923.1689.3.24 \nrjensen 2022-05-11 0:59:26 192.168.213.128 \naestrada 2022-05-09 19:28:12 1924.1680.27.57 \nasundara 2022-05-11 18:38:07 192.168.96.200 \ndkot 2022-05-12 10:52:00 1921.168.1283.75 \nabernard 2022-05-12 23:38:46 19245.168.2345.49 \ncjackson 2022-05-12 19:36:42 192.168.247.153 \njclark 2022-05-10 10:48:02 192.168.174.117 \nalevitsk 2022-05-08 12:09:10 192.16874.1390.176 \njrafael 2022-05-10 22:40:01 192.168.148.115 \nyappiah 2022-05-12 10:37:22 192.168.103.10654 \ndaquino 2022-05-08 7:02:35 192.168.168.144"

# Assign `pattern` to a regular expression that matches with all valid IP addresses and only those 
pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# Use `re.findall()` on `pattern` and `log_file` and assign `valid_ip_addresses` to the output 
valid_ip_addresses = re.findall(pattern, log_file)

# Assign `flagged_addresses` to a list of IP addresses that have been previously flagged for unusual activity
flagged_addresses = ["192.168.190.178", "192.168.96.200", "192.168.174.117", "192.168.168.144"]

# Iterative statement begins here
# Loop through `valid_ip_addresses` with `address` as the loop variable

for address in valid_ip_addresses:

    # Conditional begins here
    # If `address` belongs to `flagged_addresses`, display "The IP address ______ has been flagged for further analysis."
    if address in flagged_addresses:
        print("The IP address", address, "has been flagged for further analysis.")

    # Otherwise, display "The IP address ______ does not require further analysis."
    else:
        print("The IP address", address, "does not require for further analysis.")