# This program converts CSV to TXT

import os
import csv

def csv_to_txt(csv_path, txt_path):
    # Ensure the directory for the TXT file exists
    os.makedirs(os.path.dirname(txt_path), exist_ok=True)
    
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Create or open the output TXT file
        with open(txt_path, 'w') as txt_file:
            for row in csv_reader:
                # Join each row with a tab or space separator and write to the txt file
                txt_file.write('\t'.join(row) + '\n')

# Define the paths
csv_path = '/users/azizkhan/SQLDB/user_logins.csv'  # Replace with the actual CSV path on your system
txt_path = '/users/azizkhan/SQLDB/user_logins.txt'

# Call the function to convert CSV to TXT
csv_to_txt(csv_path, txt_path)

print(f"Conversion complete! TXT file saved at {txt_path}")
              