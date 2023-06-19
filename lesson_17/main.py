class User:

    def __init__(self, id, user_name):
        self.id = id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        user.following += 1


user_1 = User(1, "Angela")
user_2 = User(2, "Jack")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
