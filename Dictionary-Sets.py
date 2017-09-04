# Dictionaries  -  key value pairs

fruit = {"orange": "a sweet, orange, citrus fruit",
            "apple": "good for making cider",
            "lemon": "a sour, yellow citrus fruit",
            "grape": "a small, sweet fruit growing in bunches",
            "lime": "a sour, green citrus fruit"}

# print(fruit)
# print(fruit["lemon"])
#
# fruit["pear"] = "an odd shaped apple"
# print(fruit["pear"])
#
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit["lime"])

# del fruit["lemon"]
# print(fruit)
# while True:
#     dictKey = input("Please enter a fruit: ")
#     if dictKey == "quit":
#         break
#     if dictKey in fruit:
#         description = fruit.get(dictKey)
#         print(description)
#     else:
#         print("We don't have a " + dictKey)

# shorter code

# while True:
#     dictKey = input("Please enter a fruit: ")
#     if dictKey == "quit":
#         break
#     description = fruit.get(dictKey, "We don't have a " + dictKey)
#     print(description)
    # else:
    #     print("We don't have a " + dictKey)

# for snack in fruit:
#     print(fruit[snack])

# orderedKeys = sorted(list(fruit.keys()))
# # orderedKeys.sort()
# for f in orderedKeys:
#     print(f + " - " + fruit[f])

# for f in sorted(fruit.keys()):    used to sort
#     print(f + " - " + fruit[f])

# for f in fruit:
#     print(f + " - " + fruit[f])

# print(fruit)
# print(fruit.items())   # view object
# fTuple = tuple(fruit.items())
# print(fTuple)
#
# for snack in fTuple:
#     item, description = snack
#     print(item + " is " + description)
#
# print(dict(fTuple))

# ************
# list functions

# myList = ["a", "b", "c", "d"]
# letters = "abcdefghijklmnopqrstuvwxyz"
# numbers = "123456789"
#
#
# # newString = ' '
# #for c in myList:
#     # newString += c + ", "
#
# newString = ", ".join(myList)
# newLetters = ", ".join(letters)
# newNumbers = " mississippi ".join(numbers)
# print(newString)
# print(newLetters)
# print(newNumbers)
#
# locations = {0: "You are sitting in front of a computer learning Python",
#              1: "You are standing at the end of the road before a small brick building,",
#              2: "You are on top of a hill",
#              3: "You are inside a building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in a forest"}
#
# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0}}
#
# vocabulary = {"QUIT": "Q",
#               "NORTH": "N",
#               "SOUTH": "S",
#               "EAST": "E",
#               "WEST": "W"}
#

# loc = 1
# while True:
#     availableExits = ", ".join(exits[loc].keys())
#
#     print(locations[loc])
#
#     if loc == 0:
#         break
#
#     direction = input("Available exits are " + availableExits + " ").upper()
#     print()
#     if len(direction) > 1:
#         for word in vocabulary:
#             if word in direction:
#                 direction = vocabulary[word]
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print("You cannot go in that direction")

# better way
# print(locations[0].split())
# print(locations[3].split(","))
# print(" ".join(locations[0].split()))

# loc = 1
# while True:
#     availableExits = ", ".join(exits[loc].keys())
#
#     print(locations[loc])
#
#     if loc == 0:
#         break
#
#     direction = input("Available exits are " + availableExits + " ").upper()
#     print()
#     if len(direction) > 1:
#         words = direction.split()
#         for word in words:
#             if word in vocabulary:
#                 direction = vocabulary[word]
#     if direction in exits[loc]:
#         loc = exits[loc][direction]
#     else:
#         print("You cannot go in that direction")

# ******
# Added another dictionary and added a previous dictionary to it.

# locations = {0: "You are sitting in front of a computer learning Python",
#              1: "You are standing at the end of the road before a small brick building,",
#              2: "You are on top of a hill",
#              3: "You are inside a building, a well house for a small stream",
#              4: "You are in a valley beside a stream",
#              5: "You are in a forest"}
#
# namedExits = {1: {"2": 2, "3": 3, "5": 5, "4": 4},
#               2: {"5": 5},
#               3: {"1": 1},
#               4: {"1": 1, "2": 2},
#               5: {"2": 2, "1": 1}}
#
# exits = {0: {"Q": 0},
#          1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
#          2: {"N": 5, "Q": 0},
#          3: {"W": 1, "Q": 0},
#          4: {"N": 1, "W": 2, "Q": 0},
#          5: {"W": 2, "S": 1, "Q": 0}}
#
# vocabulary = {"QUIT": "Q",
#               "NORTH": "N",
#               "SOUTH": "S",
#               "EAST": "E",
#               "WEST": "W",
#               "ROAD": "1",
#               "HILL": "2",
#               "BUILDING": "3",
#               "VALLEY": "4",
#               "FOREST": "5"}
#
#
# loc = 1
# while True:
#     availableExits = ", ".join(exits[loc].keys())
#
#     print(locations[loc])
#
#     if loc == 0:
#         break
#     else:
#         allExits = exits[loc].copy()
#         allExits.update(namedExits[loc])
#
#     direction = input("Available exits are " + availableExits + " ").upper()
#     print()
#     if len(direction) > 1:
#         for word in vocabulary:
#             if word in direction:
#                 direction = vocabulary[word]
#     if direction in allExits:
#         loc = allExits[direction]
#     else:
#         print("You cannot go in that direction")
# --------------------------

# -----------SETS-------------
#
# farmAnimals = {"sheep", "cow", "hen"}
# print(farmAnimals)
#
# for animal in farmAnimals:
#     print(animal)
#
# print("=" * 40)
#
# wildAnimals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wildAnimals)
#
# for animal in wildAnimals:
#     print(animal)
#
# farmAnimals.add("horse")
# wildAnimals.add("horse")
# print(farmAnimals)
# print(wildAnimals)
#
# emptySet = set()
# emptySet.add("a")
#
# even = set(range(0, 42, 2))
# print(even)
# squaresTuple = (4, 6, 9, 16,)
# squares = set(squaresTuple)
# print(squares)
#
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squaresTuple = (4, 6, 9, 16, 25)
# squares = set(squaresTuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print('=' * 40)
#
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)
#
# # subtraction
#
# print(sorted(even))
# print(sorted(squares))
#
# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))

# remove/discard]

# even = set(range(0, 42, 2))
# print(even)
# squaresTuple = (4, 6, 9, 16,)
# squares = set(squaresTuple)
# print(squares)
#
# squares.discard(4)
# squares.remove(16)
# print(squares)
#
# squares.add(4)
# squares.add(16)
# squares.remove(9)
#
# if squares.issubset(even):
#     print("is subset")
#
# if even.issuperset(squares):
#     print("is superset")

# ----------Challenge--------------
# Create a program that takes some text and returns a list of all the characters
# in the text that are not vowels, sorted in alphabetical order

# You can either enter the text from the keyboard or initialize a string variable with the string.

testText = (input("enter a sentence: ", ))

vowels = frozenset("aeiou")
finalSet = set(testText).difference(vowels)
finalSet.discard(" ")
print(sorted(finalSet))
