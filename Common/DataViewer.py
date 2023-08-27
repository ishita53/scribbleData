import os
import sqlite3
import Common.Constants as Constants


class DataViewer:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), '..', 'Data', Constants.DATABASE_PATH)

    def view(self):
        print("VIEWING DATA FROM DATABASE \n")

        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()

            select_query = f'''
                SELECT * FROM video_data
            '''
            cursor.execute(select_query)

            data = cursor.fetchall()
            for row in data:
                print(row)

            connection.close()

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
