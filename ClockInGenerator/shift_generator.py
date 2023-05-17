import random
from datetime import datetime, timedelta


class Shift:
    def __init__(self, start_time: datetime, end_time: datetime):
        """
        Initialize a Shift object.

        Args:
            start_time (datetime): The start time of the shift.
            end_time (datetime): The end time of the shift.
        """
        self.start_time = start_time
        self.end_time = end_time

class Workday:
    def __init__(self):
        """
        Initialize a Workday object.
        """
        self.shift1 = None
        self.shift2 = None
    
    def generate_shifts(self) -> None:
        """
        Generate random shifts for the workday.
        """
        # Generate random start and end times for shift1 within the range of 9:01 AM to 12:15 PM
        start_time1 = datetime.now().replace(hour=9, minute=1) + timedelta(minutes=random.randint(0, 14))
        end_time1 = datetime.now().replace(hour=12, minute=1) + timedelta(minutes=random.randint(0, 14))

        # Calculate start time and end time for shift2 based on shift1
        start_time2 = end_time1 + timedelta(minutes=60) + timedelta(minutes=random.randint(1, 14))
        end_time2 = start_time2 + timedelta(minutes=480 - int((end_time1 - start_time1).total_seconds() / 60))
        
        # Create Shift objects for shift1 and shift2
        self.shift1 = Shift(start_time1, end_time1)
        self.shift2 = Shift(start_time2, end_time2)
            
if __name__ == '__main__':
    workday = Workday()
    workday.generate_shifts()
    # print(workday.shift1.start_time.strftime("%H:%M"))
    # print(workday.shift1.end_time.strftime("%H:%M"))
    # print(workday.shift2.start_time.strftime("%H:%M"))
    # print(workday.shift2.end_time.strftime("%H:%M"))
