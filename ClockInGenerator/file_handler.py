import json
from collections import OrderedDict

class JSONFileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data

    def write_data(self, data):
        # Load existing data
        existing_data = self.load_data()

        # Add new data to existing data
        existing_data.update(data)

        # Sort the data by date in descending order
        sorted_data = OrderedDict(
            sorted(existing_data.items(), key=lambda x: x[0], reverse=True)
        )

        # Keep only the latest 30 days
        latest_data = dict(list(sorted_data.items())[:30])

        # Write the latest data to the file
        with open(self.file_path, 'w') as file:
            json.dump(latest_data, file, indent=4)
