from DataSelector import DataSelector
from DataStore import DataStore
import Common.Constants as Constants


def main():
    data_selector = DataSelector(Constants.CSV_FILE_PATH)
    data_selector.display_attributes()
    selected_attributes = data_selector.select_attributes()

    data_store = DataStore(selected_attributes)
    data_store.read_data()
    data_store.store_in_database()

if __name__ == "__main__":
    main()
