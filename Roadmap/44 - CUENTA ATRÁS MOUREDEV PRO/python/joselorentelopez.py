import os
import time
from datetime import datetime
from threading import Thread

class Error_Handler():
    def __init__(self) -> None:
        """
        Initializes the Error_Handler class.

        This class is used to handle errors related to invalid inputs,
        ensuring that the user inputs valid values within specified ranges.
        """
        pass

    @staticmethod
    def get_valid_input(prompt, min_value, max_value):
        """
        Prompts the user for input and validates it within the given range.

        This method keeps asking the user for input until a valid integer
        within the specified range is entered.

        Args:
            prompt (str): The message displayed to the user.
            min_value (int): The minimum valid value for the input.
            max_value (int): The maximum valid value for the input.

        Returns:
            int: The valid input entered by the user.
        """
        while True:
            try:
                value = int(input(prompt))
                if value < min_value or value > max_value:
                    print(f"Please enter a value between {min_value} and {max_value}.")
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter an integer.")

class Counter():
    def __init__(self) -> None:
        """
        Initializes the Counter class.

        This class is responsible for managing the countdown process,
        including gathering user input for the target date and time,
        calculating the remaining time, and running the countdown.
        """

        self.error_handler = Error_Handler()

    def _mark_date(self):
        """
        Prompts the user to enter a target date and time for the countdown.

        This method asks the user for year, month, day, hour, minute, and second
        to specify the target date and time. It also calculates the time difference
        between the current time and the specified target time.

        Args:
            None

        Returns:
            None
        """

        current_year = datetime.now().year

        year = self.error_handler.get_valid_input("Enter the year (YYYY): ", current_year, current_year + 100)
        month = self.error_handler.get_valid_input("Enter the month (MM): ", 1, 12)

        while True:
            day = self.error_handler.get_valid_input("Enter the day (DD): ", 1, 31) 
            try:
                datetime(year, month, day)
                break
            except ValueError:
                print("Invalid day for the given month and year. Please try again.")

        hour = self.error_handler.get_valid_input("Enter the hour (24-hour format HH): ", 0, 23)
        minute = self.error_handler.get_valid_input("Enter the minute (MM): ", 0, 59)
        second = self.error_handler.get_valid_input("Enter the second (SS): ", 0, 59)

        end_time  = datetime(year, month, day, hour, minute, second)
        diff = end_time - datetime.now()

        self.days = diff.days
        self.seconds = diff.seconds

    def _counter(self):
        """
        Starts the countdown from the calculated remaining time.

        This method uses the total remaining time (in seconds) and counts down,
        updating the display every second. It also handles clearing the console
        to keep the display updated in real-time.

        Args:
            None

        Returns:
            None
        """

        total_seconds = self.days * 86400 + self.seconds

        for x in range(total_seconds, 0, -1):
            days = x // 86400  
            hours = (x % 86400) // 3600  
            minutes = (x % 3600) // 60  
            seconds = x % 60  

            # Clear the console in every iteration
            if os.name == 'posix':
                os.system('clear')

            print("{:02d}:{:02d}:{:02d}:{:02d}".format(days, hours, minutes, seconds))
            
            time.sleep(1)  

        print("Time's up!")
    
    def run(self):
        """
        Runs the complete countdown process.

        This method initiates the process by calling `_mark_date` to get the target
        time and `_counter` to start the countdown.
        """

        self._mark_date()
        self._counter()

def main():
    """
    Runs the main function of the project.
    """
    
    counter = Counter()
    counter_thread = Thread(target=counter.run())
    counter_thread.start()

if __name__ == "__main__":
    main()