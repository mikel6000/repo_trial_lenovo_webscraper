# pip install psycopg2
# pip install psycopg2-binary
# vs_buildtools.exe --norestart --passive --downloadThenInstall --includeRecommended --add Microsoft.VisualStudio.Workload.NativeDesktop --add Microsoft.VisualStudio.Workload.VCTools --add Microsoft.VisualStudio.Workload.MSBuildTools

import csv
import psycopg2

def insert_data_from_csv(csv_file_path, db_config):
    # Connect to the PostgreSQL database
    try:
        conn = psycopg2.connect(
            dbname=db_config['LenovoDA'],
            user=db_config['postgres'],
            password=db_config['common'],
            host=db_config['192.168.2.67'],
            port=db_config['5432']
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
                    "INSERT INTO test_cases_tdms (case_id, case_type, case_name, version, keywords, auto_type, workloading, priority, creator, category_folder, execution_type, status, os, phase, owner, objective, release_notes, type_matrix, case_tools) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
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
    csv_file_path = 'C:/Users/michaeljohn.roguel/Documents/GitHub/repo_trial_lenovo_webscraper/processed_TC_TDMS_data.csv'
    
    # Database configuration
    db_config = {
        'dbname': 'LenovoDA',
        'user': 'postgres',
        'password': 'common',
        'host': '192.168.2.67',
        'port': '5432'
    }

    insert_data_from_csv(csv_file_path, db_config)