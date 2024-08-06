class People:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city


n = int(input())
ppl = []
for _ in range(n):
    name, address, city = tuple(input().split())
    ppl.append(People(name, address, city))

max_idx = 0
for i in range(1, n):
    if ppl[max_idx].name < ppl[i].name:
        max_idx = i

print(f'name {ppl[max_idx].name}')
print(f'addr {ppl[max_idx].address}')
print(f'city {ppl[max_idx].city}')