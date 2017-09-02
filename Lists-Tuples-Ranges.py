# Lists
# ipAddress = input("Please enter an IP Address: ")
# print(ipAddress.count("."))

# parrotList = ["non-pinin", "no more", "a stiff", "bereft of live"]
#
# parrotList.append("A Norwegian Blue")
#
# for state in parrotList:
#     print("This parrot is " + state)
#
# even = [0, 2, 4, 6, 8]
#
# odd = [1, 3, 5, 7, 9]
#
# numbers = even + odd
# numbers.sort()  # only manipulates an object - does not create a new object
# print(sorted(numbers))


# list1 = []
# list2 = list()
#
# print("List 1: {}".format(list1))
# print("List 2: {}".format(list2))
#
# if list1 == list2:
#     print("Both lists are equal")

# even = [2, 4, 6, 8]
# anotherEven = list(even)
# print(anotherEven is even)
# print(anotherEven == even)  # returns different answer than is
# anotherEven.sort(reverse=True)
# print(even)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
#
# numbers = [even, odd]
# print(numbers)
#
# for numberSet in numbers:
#     print(numberSet)
#     for value in numberSet:
#         print(value)

# Challenge -- add to the program below so that it finds a meal without spam
# it prints out each of the ingredients of the meal

# menu = []
# menu.append(["egg", "spam", "bacon"])
# menu.append(["egg", "sausage", "bacon"])
# menu.append(["egg", "spam"])
# menu.append(["egg", "bacon", "spam"])
# menu.append(["egg", "bacon", "sausage", "spam"])
# menu.append(["spam", "bacon", "sausage", "spam"])
# menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
# menu.append(["spam", "egg", "sausage", "spam"])
#
# # print(menu)
#
# for meal in menu:
#     if not "spam" in meal:
#         for ingredients in meal:
#             print(ingredients)

# string = '1234567890'
#
# for char in string:
#     print(char)

# Ranges -- built in type

# print(range(100))  # shows how to type out that range
#
# myList = list(range(10))
# print(myList)
#
# even = list(range(0, 10, 2))  # last number is the step
# odd = list(range(1, 10, 2))
#
# print(even)
# print(odd)

# myString = "abcdefghijklmnopqrstuvwxyz"
# print(myString.index('e'))
# print(myString[4])
#
# smallDecimals = range(0, 10)
# print(smallDecimals)
# print(smallDecimals.index(3))
# print(smallDecimals[3])
#
# sevens = range(7, 10000, 7)
# x = int(input("Please enter a number less than a million: "))
# if x in sevens:
#     print("{} is divisible by seven.".format(x))
#
# print(smallDecimals)
#
# myRange = smallDecimals[::2]
# print(myRange)
# print(myRange.index(4))

# decimals = range(0, 100)
# print(decimals)
#
# myRange = decimals[3:40:3]
# print(myRange)
#
# for i in myRange:
#     print(i)
# print('=' * 40)
#
# for i in range(3, 40, 3):
#     print(i)
#
# print(myRange == range(3, 40, 3))

# r = range(0, 100)
# print(r)
#
# for i in r[::-2]:
#     print(i)
#
# print("=" * 40)
# for i in range(99, 0 , -2):
#     print(i)
#
# print("=" * 40)
# print(range(0, 100)[::2] == range(99, 0, -2))
#
# for i in range(100, 0, -2):
#     print(i)

# backString = "egaugnal lufrewop yrev a si nohtyP"
# print(backString[::-1])
#
# r = range(0, 10)
# for i in r[::-1]:
#     print(i)

# Challenge
# Experiment with different ranges and slices to get a feel for how the work.
# Remember that you can print the range as well as iterating through it to print
# its values, to check that your ranges are what you expected.
# You may also want to include things like:
# ************************8
# o = range(0, 100, 4)
# print(o)
# p = o[::5]
# print(p)
# for i in p:
#     print(i)

# and see if you can work out what will be printed before running the program.

# *********************
# Tuples -- immutable

t = "A", "B", "C"
print(t)

print("a", "b", "c")
print(("a", "b", "c"))
