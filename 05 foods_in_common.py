def foods_in_common(foods1, foods2):
    
    # a = [1, 2, 3, 4, 5, 6, 7, 8]
    # b = [12, 11, 10, 9, 8, 7, 6, 5]

        foods3 = list(set(foods1).intersection(set(foods2)))

    # Uncomment this to print / check output
    # print sorted(result)

        return sorted(foods3)

foods1 = ["cheese", "bagel", "tiramisu", "pizza", "sushi", "cake", "kale", "zebra cakes"],
foods2 = ["hummus", "sushi", "cheese", "beets", "kale", "liver", "lentils", "bagel", "cake" ]

# Call the function, run foods1 and foods2 for matches
foods_in_common(foods1, foods2)
