class Agent:
    def __init__(self, codename=0, score=0):
        self.code = codename
        self.score = score

agent = []
for _ in range(5):
     codename, score = tuple(input().split())
     agent.append(Agent(codename, int(score)))

min_idx = 0
for i in range(1, 5):
    if agent[min_idx].score > agent[i].score:
        min_idx = i

print(agent[min_idx].code, agent[min_idx].score)