
def all_odd(my_list):

    """
    Iterate a list of numbers
    Return only the odd numbers

    """

    all_odd = []

    for number in my_list:
        if (number % 2) == 1:
            all_odd.append(number)
    
    # confirm output = all odd
    print all_odd      

    # return 
    return all_odd

all_odd([1, 4, 5, 8, 11, 20, 24, 33, 55, 70, 91])
