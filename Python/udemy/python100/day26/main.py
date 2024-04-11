import pandas

nato_data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

answer_list = list(input("please enter your sentence. : ").upper())
nato_result = [nato_dict[answer_alphabet] for answer_alphabet in answer_list if answer_alphabet in list(nato_dict.keys())]
print(" ".join(nato_result))