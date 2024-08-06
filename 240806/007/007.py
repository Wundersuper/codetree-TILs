class Secret_agent:
    def __init__(self, code, location, time):
        self.code = code
        self.loc = location
        self.time = time

code, loc, time = tuple(input().split())

info = Secret_agent(code, loc, time)
print('secret code :', info.code)
print('meeting point :', info.loc)
print('time :', info.time)