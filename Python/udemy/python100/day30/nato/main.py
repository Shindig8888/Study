import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
alphabets = list(nato_dict.keys())

while True:
    try:
        answer_list = list(input("please enter your sentence. : ").upper().replace(" ", ""))
        for a in answer_list:
            if a not in alphabets:
                raise ValueError
    except ValueError:
        print("Alphabets only!")
        continue
    else:
        nato_result = [nato_dict[answer_alphabet] for answer_alphabet in answer_list if answer_alphabet in list(nato_dict.keys())]
        print(" ".join(nato_result))
        break

