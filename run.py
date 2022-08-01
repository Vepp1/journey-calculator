def get_distance():
    """
    Function to get the total journeys distance. It runs a while loop
    until the input is valid.
    """

    while True:
        distance = input("Please, enter the trip distance in km here (Ex: 1000):\n")

        if validate_data_numbers(distance):
            print("Data is valid!\n")
            break
    return int(distance)

    
    
def trip_info():
    """
    Function to determine if its a a round or one way trip.
    In case it is around, the total distance and prices wil be doubled
    on the main function.
    """
    while True:
        type = input("Is this a round tripe? (Ex: Y or N):\n")

        if validate_data_letters(type):
            print("Data is valid!\n")
            break
    return type



def validate_data_numbers(data):
    """
    Validates the numbers input provided by the user.
    """
    try:
        if data.isnumeric():
            return True
        else:
            raise ValueError(
                f"A valid number is required, you provided {data}"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False


def validate_data_letters(data):
    """
    Validates the Y/N inputs provided by the user
    """
    try:
        if data != "Y" and data != "N":
            raise ValueError(
                f"A Y or N input is required, you provided {data}"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True

def get_ticket_price():
    """
    This function get the total ticket(s) price from the
    users input.
    """
    while True:
        ticket = input("Inform the ticket(s) total price (Ex: 1000):\n")

        if validate_data_numbers(ticket):
            print("Data is valid!\n")
            break

    return int(ticket)






