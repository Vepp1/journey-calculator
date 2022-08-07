def get_distance():
    """
    Function to get the total journeys distance. It runs a while loop
    until the input is valid.
    """

    while True:
        distance = input('Please, enter the trip distance in ' +
                         'km here (Ex: 1000):\n')

        if validate_numbers(distance):
            print('Data is valid!\n')
            break
    return float(distance)


def trip_info():
    """
    Function to determine if its a a round or one way trip.
    In case it is around, the total distance and prices will be doubled
    on the main function.
    """

    while True:
        type = input('Is this a round tripe? (Ex: Y or N):\n').upper()

        if validate_letters(type):
            print('Data is valid!\n')
            break
    return type


def validate_numbers(data):
    """
    Validates the numbers input provided by the user.
    """
    try:
        float(data)
        return True
        print('Data is valid!\n')
    except:
        if not data:
            print('Invalid data: A valid number is required,' +
                  'you provided an empty value, please try again.\n')
        else:
            print(f'Invalid data: A valid number is required,' +
                  'you provided: {data}. Please try again.\n')


def validate_letters(data):
    """
    Validates the Y/N inputs provided by the user
    """

    if not data:
        print('Invalid data: A Y or N input is required,' +
              'you provided an empty value, please try again.\n')
        return False
    elif data != "Y" and data != "N":
        print(f'Invalid data: A Y or N input is required,' +
              'you provided: {data}. Please try again. \n')
        return False
    else:
        return True
        print('Data is valid!\n')


def get_ticket_price():
    """
    This function get the total ticket(s) price from the
    users input.
    """

    while True:
        ticket = input('Inform the ticket(s) total price (Ex: 1000):\n')

        if validate_numbers(ticket):
            break

    return float(ticket)


def get_car_mileage():
    """
    Collects the data about how many km the car drives
    with one liter of gasoline.
    """

    while True:
        mileage = input(
            'Please, inform how many km your car drives with 1 liter of gasoline. Normal cars drive around 12.5-15 km/l in average. (Ex: 15)\n')

        if validate_numbers(mileage):
            break
    return float(mileage)


def get_fuel_price():
    """
    The function get_gas_price, collects the actual gasolines price from
    users input.
    """

    while True:
        fuel = input('Insert the actual fuel price (Ex 2.50):\n')

        if validate_numbers(fuel):
            break
    return float(fuel)


class TripCalculator():
    """
    Class to gather all data and make the final calculation,
    to check with transportation it is cheaper for the user
    """

    def __init__(self, distance, ticket, mileage, fuel, trip):
        self.distance = distance
        self.ticket = ticket
        self.mileage = mileage
        self.fuel = fuel
        self.trip = trip

    def calculate(self):
        if self.trip == "Y":
            self.distance *= 2
            self.ticket *= 2

        car_price = round((self.distance / self.mileage) * self.fuel, 2)

        if car_price > self.ticket:
            print('A car is not the best option for this trip.\n')
            print(f'For a {self.distance}km journey, you will expend {car_price} Euro taking a car.' +
                  'While with other transportations, the price is {self.ticket}.\n')
        elif car_price < self.ticket:
            print('A car is the best option for this trip.\n')
            print(f'For a {self.distance}km journey, you will expend {car_price}' +
                  f'Euro taking a car. While with other transportations, the price is {self.ticket}.')
        else:
            print('With both options the expenses are the same!')


def main():
    """
    This function runs all the other functions to give the 
    final result.
    """

    print('Welcome to Trip Calculator!')
    print('Calculate your trip expenses and check what transportation suits you better.\n')
    distance = get_distance()
    trip = trip_info()
    ticket = get_ticket_price()
    mileage = get_car_mileage()
    fuel = get_fuel_price()
    result = TripCalculator(distance, ticket, mileage, fuel, trip)
    result.calculate()


if __name__ == "__main__":
    main()
