# s = [1, 3,5,6,7]

# for index, chr in enumerate(s):
#     print(f"ind: {index} , chr: {chr}")


dictionary = {}

# dictionary['b'] = 4


print(dictionary)

dictionary['b'] = 6 + dictionary.get('b', 0)

print(dictionary)