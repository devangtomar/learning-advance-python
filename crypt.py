import base64
string = base64.b64encode("Pogba45$".encode("utf-8"))
print(string)

print(base64.b64decode(string).decode("utf-8"))