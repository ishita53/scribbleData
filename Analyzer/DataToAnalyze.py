import sqlite3


class DataToAnalyze:

    def __init__(self, db_path):
        self.db_path = db_path

    def get_available_columns(self):
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()

            cursor.execute("PRAGMA table_info(video_data)")
            columns = [row[1] for row in cursor.fetchall()]

            connection.close()
            return columns
        except sqlite3.Error as e:
            print(f"An error occurred while fetching columns: {e}")
            return []

    def column_selector(self):
        available_columns = self.get_available_columns()

        if available_columns:
            print("Available columns:")
            for index in range(1, len(available_columns)):
                print(f"{index}. {available_columns[index]}")

            selected_column_indices = input("Enter the indices of columns (space-separated) you want to select: \n")
            selected_column_indices = [int(index) for index in selected_column_indices.strip().split()]

            if all(index in range(len(available_columns)) for index in selected_column_indices):
                selected_columns = [available_columns[index] for index in selected_column_indices]
                return selected_columns
            else:
                print("Invalid column indices.")
        else:
            print("No columns available to select.")

        return []
