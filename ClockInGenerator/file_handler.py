import json

class JSONFileHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data

    def write_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)
