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
        
        distance = input("Please, enter the trip distance here:\n")
        print(distance)

get_distance()
