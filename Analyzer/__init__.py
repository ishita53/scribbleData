import os

from Common import Constants
from DataToAnalyze import DataToAnalyze
from DataAnalyzer import DataAnalyzer


def main():
    db_path = os.path.join(os.path.dirname(__file__), '..', 'Data', Constants.DATABASE_PATH)
    data_to_analyze = DataToAnalyze(db_path)
    selected_columns = data_to_analyze.column_selector()

    data_analyzer = DataAnalyzer(db_path, selected_columns)
    data_analyzer.display_column_stats()



if __name__ == "__main__":
    main()
