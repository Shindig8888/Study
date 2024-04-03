# class User:
#     def __init__(self):
#         pass
#     pass

# user_1 = User()
# user_1.id = '001'
# print(user_1.id)

#PascalCase
#camelCase
#snake_case


# class User:
#     def __init__(self, id:str, username:str):
#         self.id = id
#         self.username = username
#         self.follower = 0




# user_1 = User('001', 'Shin')
# print(user_1.id)
# print(user_1.username)
# print(user_1.follower)

# user_2 = User('002', 'Dig')
# print(user_2.id)
# print(user_2.username)



class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User('001', 'shin')
user_2 = User('002', 'dig')

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)