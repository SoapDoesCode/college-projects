def convert_days(num_days: float, to_format = "hours") -> float|str:
    """Input your number of days and this function will return how many hours, minutes, and seconds that translates to
    
    Examples:
    > convert_date(10, "hours")
    240
    > convert_date(10, "hours")
    14400
    > convert_date(10, "hours")
    864000
    """
    to_format = to_format.lower() # makes sure the input is in the correct case, makes checks easier

    if to_format == "hours": # checks if converting to hours
        return num_days * 24
    elif to_format == "minutes": # checks if converting to minutes
        return num_days * 1440
    elif to_format == "seconds": # checks if converting to seconds
        return num_days * 86400
    else:
        return "That is not a valid output format! Please use either 'hours', 'minutes' or 'seconds'"

if __name__ == "__main__":
    converted_hours = convert_days(10, "hours") # runs the conversion function
    converted_mins = convert_days(10, "minutes") # runs the conversion function
    converted_sec = convert_days(10, "seconds") # runs the conversion function

    print(f"Hours: {converted_hours}") # prints the output to terminal
    print(f"Minutes: {converted_mins}") # prints the output to terminal
    print(f"Seconds: {converted_sec}") # prints the output to terminal