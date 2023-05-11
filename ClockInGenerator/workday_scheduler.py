from datetime import datetime, timedelta
from dateutil import parser
from file_handler import JSONFileManager, JSONDataProcessor
from shift_generator import Workday


class ShiftManager:
    def __init__(self, file_name: str):
        """
        Initializes the ShiftManager object.

        Args:
            file_name (str): The name of the JSON file to handle.
        """
        self.file_handler = JSONFileManager(file_name)

    def load_data(self):
        """
        Loads data from the JSON file.

        Returns:
            dict: The loaded data from the JSON file.
        """
        return self.file_handler.load_data()

    def get_most_recent_date(self, data: dict) -> datetime:
        """
        Returns the most recent date from the provided data.

        Args:
            data (dict): The data dictionary.

        Returns:
            datetime: The most recent date.
        """
        dates = [parser.parse(date) for date in data.keys()]
        return max(dates)

    def calculate_working_days(self, most_recent_date: datetime) -> int:
        """
        Calculates the number of working days between the most recent date and today.

        Args:
            most_recent_date (datetime): The most recent date.

        Returns:
            int: The number of working days.
        """
        today = datetime.now().date()
        if today.weekday() >= 5:
            days_to_subtract = today.weekday() - 4
            today -= timedelta(days=days_to_subtract)

        working_days = 0
        current_date = most_recent_date.date()
        while current_date != today:
            current_date += timedelta(days=1)
            if current_date.weekday() < 5:
                working_days += 1

        return working_days

    def update_last_8_days(
        self,
        last_8_days: dict,
        shift1_start: str,
        shift1_end: str,
        shift2_start: str,
        shift2_end: str
    ):
        """
        Updates the last 8 days' shift information with the provided shift data.

        Args:
            last_8_days (dict): The dictionary containing the last 8 days' shift data.
            shift1_start (str): The start time of shift 1.
            shift1_end (str): The end time of shift 1.
            shift2_start (str): The start time of shift 2.
            shift2_end (str): The end time of shift 2.
        """
        last_8_days['input01'].append(shift1_start)
        last_8_days['exit01'].append(shift1_end)
        last_8_days['input02'].append(shift2_start)
        last_8_days['exit02'].append(shift2_end)

        if len(last_8_days['input01']) > 8:
            last_8_days['input01'] = last_8_days['input01'][-8:]
            last_8_days['exit01'] = last_8_days['exit01'][-8:]
            last_8_days['input02'] = last_8_days['input02'][-8:]
            last_8_days['exit02'] = last_8_days['exit02'][-8:]

    def generate_shifts(self, last_8_days: dict) -> tuple[str, str, str, str]:
        """
        Generates shifts and returns the shift times.

        Args:
            last_8_days (dict): The dictionary containing the last 8 days' shift data.

        Returns:
            tuple[str, str, str, str]: The start and end times of shift 1 and shift 2.
        """
        workday = Workday()
        while True:
            workday.generate_shifts()
            shift1_start = workday.shift1.start_time.strftime('%H:%M')
            shift1_end = workday.shift1.end_time.strftime('%H:%M')
            shift2_start = workday.shift2.start_time.strftime('%H:%M')
            shift2_end = workday.shift2.end_time.strftime('%H:%M')

            if shift1_start not in last_8_days['input01'] \
                    and shift1_end not in last_8_days['exit01'] \
                    and shift2_start not in last_8_days['input02'] \
                    and shift2_end not in last_8_days['exit02']:
                return shift1_start, shift1_end, shift2_start, shift2_end

    def add_shift_data(
        self,
        data: dict,
        current_date: datetime,
        shift1_start: str,
        shift1_end: str,
        shift2_start: str,
        shift2_end: str
    ):
        """
        Adds shift data to the data dictionary.

        Args:
            data (dict): The data dictionary.
            current_date (datetime): The current date.
            shift1_start (str): The start time of shift 1.
            shift1_end (str): The end time of shift 1.
            shift2_start (str): The start time of shift 2.
            shift2_end (str): The end time of shift 2.
        """
        data[current_date.strftime('%m/%d')] = {
            'input01': shift1_start,
            'exit01': shift1_end,
            'input02': shift2_start,
            'exit02': shift2_end,
        }

    def process_shifts(self):
        """
        Processes shifts by generating new shifts and updating the data.

        This method loads data, calculates the most recent date, calculates the number of working days,
        generates shifts for each working day, updates the last 8 days' shift data, and adds the shift data
        to the loaded data. Finally, it saves the updated data to the JSON file.
        """
        data = self.load_data()
        most_recent_date = self.get_most_recent_date(data)
        working_days = self.calculate_working_days(most_recent_date)

        current_date = most_recent_date
        last_8_days = {
            'input01': [],
            'exit01': [],
            'input02': [],
            'exit02': []
        }

        while working_days > 0:
            current_date += timedelta(days=1)
            if current_date.weekday() < 5:
                shift1_start, shift1_end, shift2_start, shift2_end = self.generate_shifts(last_8_days)
                self.update_last_8_days(last_8_days, shift1_start, shift1_end, shift2_start, shift2_end)
                self.add_shift_data(data, current_date, shift1_start, shift1_end, shift2_start, shift2_end)
                working_days -= 1

        data_processor = JSONDataProcessor(self.file_handler)
        data_processor.add_data(data)

if __name__ == '__main__':
    shift_manager = ShiftManager('employee_work_hours.json')
    shift_manager.process_shifts()