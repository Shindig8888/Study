#list comprehension

# list_num =  ['1 ','2 ','3' ]
# new_list = [2*int(item.strip()) for item in list_num]
# print(new_list)

# name = 'Angela'
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [number*2 for number in range(1,5)]
# print(new_list)

# new_list = [number*2 for number in range(1,5) if number%2 == 0]
# print(new_list)

# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# long_name = [name.upper() for name in names if len(name)>=5 ]
# print(long_name)

# if answer_state == 'Exit':
#     missings_staes = [state for state in all_states if state not in guessed state]


## dictionary comprehensions
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}


# import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# new_dict = {name : random.randint(1, 100) for name in names}
# print(new_dict)
# passed_students = {student:score for (student, score) in new_dict.items() if score>=60}
# print(passed_students)


#pandas loop

# import pandas

# student_dict = {
#     'student' : ['Angela', 'James', "Lily"],
#     'score' : [56, 76, 98]
# }

# student_data = pandas.DataFrame(student_dict)
# print(student_data)
# for (key,value) in student_data.items():
#     print(value)

# #iterrow
# for (index,row) in student_data.iterrows():
#     if row.student == 'Angela':
#         print(row.score)
