import mysql.connector
import csv

# Function to generate SQL insert statements
def generate_sql_inserts(csv_file, table_name):
    sql_inserts = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            values = [f"'{row[key]}'" if key != 'Transaction Activity' else row[key] for key in row]
            sql_insert = f"INSERT INTO {table_name} ({', '.join(row.keys())}) VALUES ({', '.join(values)});"
            sql_inserts.append(sql_insert)
    return sql_inserts

# CSV file name and table name
csv_file = 'Maphlix_Trust_Ghana_Ltd_Data.CSV'  # Replace 'your_csv_file.csv' with your CSV file name
table_name = 'YourTableName'     # Replace 'YourTableName' with your table name

#establish connection with database
connection = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='db')
print("DB connected")

cursor = connection.cursor()

# CSV file name and table name
csv_file = 'Maphlix_Trust_Ghana_Ltd_Data.CSV'  # Replace 'your_csv_file.csv' with your CSV file name
table_name = 'MaphlixData'     # Replace 'YourTableName' with your table name

# Generate SQL insert statements
sql_inserts = generate_sql_inserts(csv_file, table_name)

# Print the generated SQL insert statements
for insert_statement in sql_inserts:
    cursor.execute(insert_statement)

connection.commit()
connection.close()

