# def format_name(f_name, l_name):
#     """Take a first and last name and format it 
#     to return the title case version of the name"""
#     if f_name == '' or l_name == '':
#         return 'Please wright valid name'
#     f_name = f_name.title()
#     l_name = l_name.title()
#     return f_name + " " + l_name

# print(format_name("SHIN", 'donggil'))

# format_name()

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

try_value = False
while True:
    print(logo)
    print("\nWelcome to my Calculator!")
    while True:
        if not try_value:
            try:
                first_num = float(input("\nEnter first number : "))
                
            except ValueError:
                print('\nPlease Enter numbers only')
                continue
            else:
                break        
        else:
            break
    while True:
        functype = input("\nEnter type of function you need(+,-,*,/) : ")
        if functype == '+' or functype == '-' or functype == '*' or functype == '/':
            break
        else:
            print("\nPlease enter only '-', '+', '*', '/'")
            continue

    while True:
        try:
            second_num = float(input("\nEnter second number : "))
        except ValueError:
            print('\nPlease Enter numbers only')
            continue
        else:
            break    


    def calculator(firstnumber, functiontype, secondnumber):
        if functiontype == '+':
            return firstnumber + secondnumber
        elif functiontype == '-':
            return firstnumber - secondnumber
        elif functiontype == '*':
            return firstnumber * secondnumber
        elif functiontype == '/':
            if secondnumber==0:
                return '\nYou cannot devide by 0'
            else:
                return round(firstnumber / secondnumber, 2)

    result = calculator(first_num,functype,second_num)
    print(f"\n {first_num} {functype} {second_num} = {result}")
    try_again = input("\nDo you want to use calculator with result?(Y/N) : ").lower()
    if try_again == 'y':
        try_value = True
        result = first_num
        continue
    elif try_again == 'n':
        try_value = False
        break
print('\nThanks for using my calculator!')
