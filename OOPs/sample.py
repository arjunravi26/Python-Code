class User:
    def __init__(self, id, name):
        self.names = name
        self.id = id
        self.following = 0
        self.followers = 0
        print(f"New user is created with id {id} and name: {name} ")

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(1, "Arjun")
user_2 = User(2, "Jishnu")
user_2.follow(user_1)

print(f"User {user_1.names}")
print(f"has {user_1.followers} followers")
print(f"has {user_1.following} followers")

print(f"User {user_2.names}")
print(f"has {user_2.followers} followers")
print(f"has {user_2.following} followers")

user_1.follow(user_2)
print(f"User {user_1.names}")
print(f"has {user_1.followers} followers")
print(f"has {user_1.following} followers")

print(f"User {user_2.names}")
print(f"has {user_2.followers} followers")
print(f"has {user_2.following} followers")
