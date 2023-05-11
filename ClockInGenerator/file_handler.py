import json
from collections import OrderedDict


class JSONFileManager:
    """Handles reading and writing data to a JSON file."""

    def __init__(self, file_path: str):
        """
        Initialize JSONFileManager.

        Args:
            file_path (str): The path to the JSON file.
        """
        self.file_path = file_path

    def load_data(self) -> dict:
        """
        Load data from the JSON file.

        Returns:
            dict: The loaded JSON data.
        """
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        return data

    def write_data(self, data: dict) -> None:
        """
        Write data to the JSON file.

        Args:
            data (dict): The data to be written to the JSON file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(data, file, indent=4)


class JSONDataProcessor:
    """Handles data manipulation and updates in the JSON file."""

    def __init__(self, file_manager: JSONFileManager):
        """
        Initialize JSONDataProcessor.

        Args:
            file_manager (JSONFileManager): The instance of JSONFileManager to handle file operations.
        """
        self.file_manager = file_manager

    def add_data(self, new_data: dict) -> None:
        """
        Add new data to the JSON file.

        Args:
            new_data (dict): The new data to be added to the JSON file.
        """
        # Load existing data
        existing_data = self.file_manager.load_data()

        # Add new data to existing data
        existing_data.update(new_data)

        # Sort the data by date in descending order
        sorted_data = OrderedDict(
            sorted(existing_data.items(), key=lambda x: x[0], reverse=True)
        )

        # Keep only the latest 30 days
        latest_data = dict(list(sorted_data.items())[:30])

        # Write the latest data to the file
        self.file_manager.write_data(latest_data)


if __name__ == '__main__':
    file_manager = JSONFileManager('file_path')
    data_processor = JSONDataProcessor(file_manager)