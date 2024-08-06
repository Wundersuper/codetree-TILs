class Userlevel:
    def __init__(self, username, level):
        self.user = username
        self.level = level

user1 = Userlevel('codetree', 10)

username, level = tuple(input().split())
user2 = Userlevel(username, level)

print(f'user {user1.user} lv {user1.level}')
print(f'user {user2.user} lv {user2.level}')