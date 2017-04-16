
items = ["you", "z", "are", "z", "good", "z", "at", "x", "code"]

def every_other_item(items):
    """Return every other item in `items`, starting at first item.

    For example::

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["pickle", "pickle", "juice", "pickle", "juice", "pop"])
       ['pickle', 'juice', 'juice']

       >>> every_other_item(
       ...   ["you", "z", "are", "z", "good", "z", "at", "x", "code"]
       ... )
       ['you', 'are', 'good', 'at', 'code']
    """

    # Create a new list ITEMS2 that contains every other word in source list ITEMS
    # Start at items[0]
    items2 = items[::2]

    # Uncomment the line below to test output
    # print items2 
    return items2

every_other_item(items)

