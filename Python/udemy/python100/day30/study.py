# errors and exceptions

# try:
#     with open("a_file.txt") as file:
#         file.read()
# except FileNotFoundError:
#     with open("a_file.txt", 'w') as file:
#         file.write('')
#     print("There was a file not found error. Generated a new file.")

height = float(input("Height: "))
weight = float(input("Weight: "))


if height > 3:
    raise ValueError("Height must under 3m.")
bmi = weight / height**2