import sqlite3

class DataAnalyzer:
    def __init__(self, db_path, columns):
        self.db_path = db_path
        self.columns = columns

    def get_column_stats(self, column_name, stat_type):
        try:
            connection = sqlite3.connect(self.db_path)
            cursor = connection.cursor()

            aggregate_function = None
            if stat_type == "max":
                aggregate_function = "MAX"
            elif stat_type == "min":
                aggregate_function = "MIN"
            elif stat_type == "average":
                aggregate_function = "AVG"

            if aggregate_function:
                query = f"SELECT video_id, {aggregate_function}({column_name}) FROM video_data GROUP BY video_id ORDER BY {aggregate_function}({column_name}) DESC LIMIT 5"
                cursor.execute(query)
                result = cursor.fetchall()

                connection.close()
                return result
            else:
                print("Invalid statistic type.")
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return []

    def display_column_stats(self):
        for column in self.columns:
            print(f"Column: {column}")
            print("1. Max")
            print("2. Min")
            print("3. Average")
            choice = input("Select a statistic option (1/2/3): ")

            if choice == "1":
                stat_type = "max"
            elif choice == "2":
                stat_type = "min"
            elif choice == "3":
                stat_type = "average"
            else:
                print("Invalid choice.")
                continue

            stats = self.get_column_stats(column, stat_type)
            if stats:
                print(f"Top 5 elements based on {stat_type} {column} (Video IDs):")
                for stat in stats:
                    print(stat[0])  # Print the Video ID
            else:
                print("No data available.")
