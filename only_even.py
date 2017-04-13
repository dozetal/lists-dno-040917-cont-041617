def even_numbers(my_list):

    """

    Iterate a list of numbers 
    Return only the even numbers 

    """

    even_numbers = []

    for number in my_list:
        if (number % 2) == 1:
            even_numbers.append(number)
    
    print even_numbers 

even_numbers([1, 2, 3, 55, 62, 70, 80, 4])