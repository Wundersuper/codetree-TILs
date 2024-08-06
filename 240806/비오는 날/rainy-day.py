class Weather:
    def __init__(self, date, day, prediction):
        self.date = date
        self.day = day
        self.pred = prediction


n = int(input())
arr = [tuple(input().split()) for _ in range(n)]
weather_pred = [
    Weather(date, day, prediction)
    for date, day, prediction in arr
]

ans = Weather("9999-99-99", "", "")

for i in range(n):
    if weather_pred[i].pred == 'Rain':
        if ans.date >= weather_pred[i].date:
            ans = weather_pred[i]

print(ans.date, ans.day, ans.pred)