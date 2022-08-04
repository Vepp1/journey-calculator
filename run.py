def get_distance():
    """
    Function to get the total journeys distance. It runs a while loop
    until the input is valid.
    """

    while True:
        distance = input("Please, enter the trip distance in km here (Ex: 1000):\n")

        if validate_distance(distance):
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
        type = input("Is this a round tripe? (Ex: Y or N):\n").upper()

        if validate_data_letters(type):
            print("Data is valid!\n")
            break
    return type



def validate_distance(data):
    """
    Validates the numbers input provided by the user.
    """
    if data.isnumeric():
        return True
    elif not data:
        print(f"Invalid data: A valid number is required, you provided an empty value, please try again.\n")
        return False
    else:
        print(f"Invalid data: A valid number is required, you provided {data}, please try again.\n")


def validate_data_letters(data):
    """
    Validates the Y/N inputs provided by the user
    """
    if not data:
        print(f"Invalid data: A valid number is required, you provided an empty value, please try again.\n")
        return False
    elif data != "Y" and data != "N":
        print(f"Invalid data: A Y or N input is required, you provided {data}, please try again. \n")
        return False
    else:
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

def get_car_mileage():
    """
    Collects the data about how many km the car drives
    with one liter of gasoline.
    """

    while True:
        mileage = input("Please, inform how many km your car drives with 1 liter of gasoline. Normal cars drive aroun 12.5-15 km/l in average. (Ex: 15)\n")

        if validate_data_numbers(mileage):
            print("Data is valid!\n")
            break
    return int(mileage)

def get_gas_price():
    """
    The function get_gas_price, collects the actual gasolines price from
    users input.
    """

    while True:
        gas = input("Insert the actual gasoline price (Ex 2.50):\n")

        if validate_data_numbers(gas):
            print("Data is valid!\n")
            break
    return float(gas)

def calculate(dist, pr, mg, gs):
    """
    Function to gather all data and make the final calculation,
    to check with transportation it is cheaper for the user
    """    
    car_price = round((dist / mg) * gs, 2)

    if car_price > pr:
        print("A car is not the best option for this trip.\n")
        print(f"For a {dist}km journey, you will expend {car_price} Euro taking a car. While with other transportations, the price is {pr}.")
    elif car_price < pr:
        print("A car is the best option for this trip.\n")
        print(f"For a {dist}km journey, you will expend {car_price} Euro taking a car. While with other transportations, the price is {pr}.")
    else:
        print("With both options the expenses are the same!")

def main():
    """
    This function runs all the other functions to give the 
    final result.
    """

    print("Welcome to Trip Calculator!")
    print("Calculate your trip expenses and check what transportation suits you better.\n")
    distance = get_distance()
    trip = trip_info()
    price = get_ticket_price()
    mileage = get_car_mileage()
    gas = get_gas_price()

    if trip == "Y":
        distance *= 2
        price *= 2

    final_calcule = calculate(distance, price, mileage, gas)

main()






