import pandas as pd


class DataSelector:
    def __init__(self, csv_file_path):
        self.df = pd.read_csv(csv_file_path)
        self.attribute_titles = self.df.columns.tolist()

    def display_attributes(self):
        for idx, title in enumerate(self.attribute_titles[1:], start=1):
            print(f"Attribute {idx}: {title}")

    def display_selected_attributes(self, attributes):
        print("SELECTED ATTRIBUTES: ")
        for attribute in attributes:
            print(attribute, end=' ')
        print('\n')

    def select_attributes(self):
        print("\n PLEASE ENTER THE ATTRIBUTE NUMBERS YOU WISH TO STORE (separated by spaces): \n")
        selected_indices = input().strip().split()
        selected_attributes = [self.attribute_titles[0]]  # Vido ID will always be added

        for idx in selected_indices:
            try:
                index = int(idx)
                if 1 <= index < len(self.attribute_titles):
                    selected_attributes.append(self.attribute_titles[index])
                else:
                    print(f"Invalid index: {idx}")
            except ValueError:
                print(f"Invalid input: {idx}")
        self.display_selected_attributes(selected_attributes)

        return selected_attributes
