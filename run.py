def get_distance():
    """
    First function to be loaded. 
    Contains an explanation of how the application works and
    get the total distance input from the user.
    Run a while loop to check the validity of data.
    """

    while True:
        print("Welcome to Trip Calculator!")
        print("Calculate your trip expenses and check what transportation suits your better.\n")
        
        distance = input("Please, enter the trip distance in km here (Ex: 1000):\n")

        if validate_data_numbers(distance):
            print("Data is valid!\n")
            break

    while True:
        type = input("Is this a round tripe? (Ex: Y or N):\n")

        if validate_data_letters(type):
            print("Data is valid!\n")
            break
    
    if type == "Y":
        new_distance = int(distance) * 2
        print(new_distance)
    else:
        print(distance)



def validate_data_numbers(data):
    try:
        if data.isnumeric():
            return True
        else:
            raise ValueError(
                f"A valid number is required, you provided {data}"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        return False


def validate_data_letters(data):
    try:
        if data != "Y" and data != "N":
            raise ValueError(
                f"A Y or N input is required, you provided {data}"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        return False

    return True

get_distance()


