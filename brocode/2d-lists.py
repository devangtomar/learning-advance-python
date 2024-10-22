fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "lettuce", "onion"]
meats = ["beef", "chicken", "pork"]

grocery_list = [fruits, vegetables, meats]

print(grocery_list)
print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[2])
print(grocery_list[0][0])
print(grocery_list[0][1])
print(grocery_list[0][2])
print(grocery_list[1][0])

for collection in grocery_list:
    for item in collection:
        print(item)
