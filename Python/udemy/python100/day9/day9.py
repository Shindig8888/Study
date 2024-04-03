# # programming_dictionanry = {
# #   'Bug':'An error in a program that prevents the program from running as expected',
# #   'Function': 'Apiece of code that you can easily call over and over agian.',
# # }

# # # print(programming_dictionanry['Bug'])

# # #adding new

# # print(programming_dictionanry)
# # programming_dictionanry['Loop'] = 'The action of doing somethinf over and over again'
# # print(programming_dictionanry)

# # empty_dict = {}

# # #edit
# # print(programming_dictionanry)
# # programming_dictionanry['Bug'] = 'insect'
# # print(programming_dictionanry)

# # #Loop through dictionary

# # for thing in programming_dictionanry:
# #   print(thing)
# #   print(programming_dictionanry[thing])
# #   print(thing, 'is', programming_dictionanry[thing])

# #nesting

# caplitals = {
#   "France" : 'Paris',
#   'Germany' : 'Berlin'
# }

# travel_log = {
#   "France":['paris', 'Lille', 'Dijon'],
#   'Germany':['Berlin', 'Hamburg', 'Stuttgart']
# }

# travel_log = {
#   'country':"France",
#   'visited_cities':['paris', 'Lille', 'Dijon'], 
#   'total_visits' : 12},
#   'country':'Germany',
#   'visited_cities': ['Berlin', 'Hamburg', 'Stuttgart'],
#   'total_visits' : 12
# }

# #nesting dictionary in a list

# travel_log = []




logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

while True:
  print(logo)
  print("\nWelcome to secrete bidding program!")
  bid_dict = {}
  while True:
    name = input("\nwhat is your name? : ")
    if name in bid_dict:
      name += '2'
    bid = int(input("\nwhat is your bid? : $ "))
    bid_dict.update({name:bid})
    print(bid_dict)
    any_bidder = input('\nDo you have another bidder?(y/n) : ').lower()
    if any_bidder == 'y':
      continue
    if any_bidder == 'n':
      break
  max_bidder = max(bid_dict, key=bid_dict.get)
  print(f'\nHighest bidder is {max_bidder}, and the bid is ${bid_dict[max_bidder]}!!')
  retry = input("\nrun program again?(y/n)").lower()
  if retry == 'y':
    continue
  if retry == 'n':
    break
print('\nThank you for using my program!')