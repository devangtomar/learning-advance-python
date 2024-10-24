capitals = {"USA": "Washington DC", "France": "Paris", "India": "New Delhi"}

capitals["USA"]  # Washington DC
capitals["France"]  # Paris
capitals["India"]  # New Delhi

print(capitals.get("France"))  # Paris
print(capitals.get("Germany"))  # None

capitals["Germany"] = "Berlin"
print(capitals)

capitals["Germany"] = "Berlin"
print(capitals)

del capitals["Germany"]
print(capitals)

capitals.clear()
print(capitals)

del capitals

for key in capitals:
    print(key)

for keys in capitals.keys():
    print(keys)

for values in capitals.values():
    print(values)

for key, value in capitals.items():
    print(key, value)
