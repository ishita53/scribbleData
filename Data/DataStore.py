import sqlite3
import os
import pandas as pd
import Common.Constants as Constants


class DataStore:
    def __init__(self, selected_attributes):
        self.source_path = Constants.DATA_SOURCE
        self.db_path = Constants.DATABASE_PATH
        self.selected_attributes = selected_attributes
        self.__data = []

    def read_data(self):
        files = os.listdir(self.source_path)
        csv_files = [file for file in files if file.endswith(".csv")]

        for csv_file in csv_files:
            csv_file_path = os.path.join(self.source_path, csv_file)

            try:
                data = pd.read_csv(csv_file_path, usecols=self.selected_attributes, encoding=Constants.ENCODING)
                self.__data.append(data.values.tolist())
            except UnicodeDecodeError:
                print(f"Could not read {csv_file} due to encoding issues.")

    def store_in_database(self):
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()

            # Generate the CREATE TABLE query dynamically based on selected attributes
            create_table_query = f'''
                CREATE TABLE IF NOT EXISTS video_data (
                    video_id TEXT PRIMARY KEY,
                    {', '.join(f'{attr} TEXT' for attr in self.selected_attributes[1:])}
                )
            '''
            cursor.execute(create_table_query)

            # Insert data into the table using individual execute statements
            insert_query = f'''
                INSERT INTO video_data ({', '.join(self.selected_attributes)})
                VALUES ({', '.join(['?'] * len(self.selected_attributes))})
            '''

            for entry in self.__data:
                for row in entry:
                    try:
                        cursor.execute(insert_query, row)  # Include video_id in the values
                    except sqlite3.IntegrityError as unique_error:
                        print(f"Error: Duplicate entry detected for video_id {row[0]}. Skipping.")

            # Commit changes and close the connection
            connection.commit()
            connection.close()

            print("Data stored in the database.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
