class Bomb:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = line_color
        self.sec = second

code, line_color, second = tuple(input().split())
bomb = Bomb(code, line_color, int(second))

print(f'code : {bomb.code}')
print(f'color : {bomb.color}')
print(f'second : {bomb.sec}')