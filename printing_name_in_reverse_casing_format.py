fullname = input("Enter your fullname: ")

reversed_casing = ""

for char in fullname:
    if char.islower():
        reversed_casing += char.upper()
    else:
        reversed_casing += char.lower()

print("Output:", reversed_casing)