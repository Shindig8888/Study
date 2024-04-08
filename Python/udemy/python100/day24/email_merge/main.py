with open(r'input\Names\invited_names.txt', 'r') as name_file: 
    list_of_names = name_file.readlines()

list_of_names = list(map(str.strip, list_of_names))

for names in list_of_names:
    with open(fr'Output\ReadyToSend\letter_for_{names}.txt', 'w') as new_file:
        letter = f"Dear {names},\n\nYou are invited to my birthday this Saturday.\n\nHope you can make it!\n\nAngela"
        new_file.write(letter)