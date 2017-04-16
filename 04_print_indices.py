def print_indices(cars):

    """
    Print index of each item in list, followed by item itself.

    """

    # Identify the index for each item in list
    # Print index + item
    
    for i in range(len(cars)):
        print "%s %s" % (i, cars[i])   

cars = (["Toyota", "Jeep", "Toyota", "Volvo"])

print_indices(cars)

