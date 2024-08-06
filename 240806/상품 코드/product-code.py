class Item:
    def __init__(self, name="", code=0):
        self.name = name
        self.code = code

item1 = Item()
item1.name = 'codetree'
item1.code = 50

name, code = tuple(input().split())
item2 = Item(name, int(code))

print(f'product {item1.code} is {item1.name}')
print(f'product {item2.code} is {item2.name}')