# This program converts CSV to SQL

import os
import csv

def csv_to_sql(csv_path, sql_path, table_name):
    # Ensure the directory for the SQL file exists
    os.makedirs(os.path.dirname(sql_path), exist_ok=True)
    
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        
        # Extract headers for column names
        headers = next(csv_reader)
        
        # Open the SQL file for writing
        with open(sql_path, 'w') as sql_file:
            # Write the beginning of the SQL file
            sql_file.write(f'-- SQL insert statements for {table_name} table\n\n')
            sql_file.write(f'CREATE TABLE IF NOT EXISTS {table_name} (\n')
            sql_file.write('    id INTEGER PRIMARY KEY AUTOINCREMENT,\n')
            sql_file.write(',\n'.join([f'    {header} TEXT' for header in headers[1:]]) + '\n')
            sql_file.write(');\n\n')
            
            # Generate and write insert statements
            for row in csv_reader:
                values = ', '.join([f"'{value}'" for value in row[1:]])  # Skip ID for auto-increment
                sql_file.write(f"INSERT INTO {table_name} ({', '.join(headers[1:])}) VALUES ({values});\n")
    
    print(f"SQL file created at {sql_path}")

# Define the paths
csv_path = '/users/azizkhan/SQLDB/user_logins.csv'  # Replace with the actual CSV path on your system
sql_path = '/users/azizkhan/SQLDB/user_logins.sql'
table_name = 'users_logins'

# Call the function to convert CSV to SQL
csv_to_sql(csv_path, sql_path, table_name)

print(f"Conversion complete! SQL file saved at {sql_path}")


