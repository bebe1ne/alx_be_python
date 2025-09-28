from datetime import datetime, timedelta

def display_current_datetime():
    # Obtain the current date and time
    current_date = datetime.now()
    # Print the current date and time in the specified format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    # Prompt the user for a number of days
    try:
        number_of_days = int(input("Enter the number of days to add to the current date: "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    # Calculate the future date
    future_date = datetime.now() + timedelta=number_of_days)
    # Print the future date in the specified format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()