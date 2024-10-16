import csv
import psycopg2

def insert_data_from_csv(csv_file_path, db_config):
    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(
            dbname=db_config['dbname'],
            user=db_config['user'],
            password=db_config['password'],
            host=db_config['host'],
            port=db_config['port']
        )
        cursor = conn.cursor()

        # Open the CSV file
        with open(csv_file_path, 'r') as csv_file:
            # Skip the header row if your CSV has one
            next(csv_file)

            # Read the CSV file
            csv_reader = csv.reader(csv_file)

            # Iterate through the rows and insert them into the database
            for row in csv_reader:
                cursor.execute(
                    "INSERT INTO your_table_name (column1, column2, column3) VALUES (%s, %s, %s)",
                    row
                )

        # Commit the transaction
        conn.commit()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    # Path to your CSV file
    csv_file_path = 'path/to/your/file.csv'
    
    # Database configuration
    db_config = {
        'dbname': 'your_database',
        'user': 'your_username',
        'password': 'your_password',
        'host': 'localhost',  # or your database host
        'port': '5432'        # default PostgreSQL port
    }

    insert_data_from_csv(csv_file_path, db_config)