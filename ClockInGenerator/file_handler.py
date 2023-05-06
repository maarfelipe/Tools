import json

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

        # Remove oldest entries if there are more than 30 days
        if len(existing_data) > 30:
            sorted_dates = sorted(existing_data.keys())
            oldest_dates = sorted_dates[:len(existing_data) - 30]
            existing_data = {date: existing_data[date] for date in existing_data if date not in oldest_dates}

        # Write updated data to the file
        with open(self.file_path, 'w') as file:
            json.dump(existing_data, file, indent=4)
