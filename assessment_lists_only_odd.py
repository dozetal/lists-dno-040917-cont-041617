"""List Assessment 

Edit the functions until the doctests pass when
you run this file.

"""

def all_odd(numbers):
    """
    Return a list of only 
    the odd numbers in the input list.

    For example::

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []
    """

# Create a list of numbers
numbers = ([1, 2, 7, 8, 40, 66, 91, 101])

# Iterate through the list
for number in numbers: 

    # If number is odd, append it to the list only_odd
    # If it is not odd, return None
    # return only_odd
    if numbers((number % 2)!== 0):
        only_odd.append

    else:
        None

    return only_odd

#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nTEST PASSED. GOOD WORK!\n")
