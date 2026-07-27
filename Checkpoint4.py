# Checkpoint4

import math
from decimal import Decimal

# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

my_list = ["turmalina", "amatista", "cuarzo"]
my_tuple = ("manzanas", "peras", "naranjas")
my_float = 9.15
my_integer = 2
my_decimal = Decimal("25.5")
my_dictionary = {"videojuego": "Gta",
                 "numero": "VI", "plataforma": "Playstation"}


# Exercise 2: Round your float up.

my_float = 9.15
float_up = math.ceil(my_float)
print(float_up)

# Exercise 3: Get the square root of your float.

square_root = math.sqrt(my_float)
print(square_root)

# Exercise 4: Select the first element from your dictionary.

my_selection = list(my_dictionary.keys())[0]
my_firstvalue = my_dictionary[my_selection]
print(my_selection)
print(my_firstvalue)

# Exercise 5: Select the second element from your tuple.

second_element = my_tuple[1]
print(second_element)

# Exercise 6: Add an element to the end of your list

my_list.append("opalo")
print(my_list)

# Exercise 7: Replace the first element in your list.
my_list[0] = "lapizlazuli"
print(my_list)


# Exercise 8: Sort your list alphabetically.
my_list.sort()
print(my_list)

# Exercise 9: Use reassignment to add an element to your tuple.
my_tuple += ("blueberries",)
print(my_tuple)

