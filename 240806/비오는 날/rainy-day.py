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

for i in range(n):
    if weather_pred[i].pred == 'Rain':
        min_idx = i
        break

print(weather_pred[min_idx].date, weather_pred[min_idx].day, weather_pred[min_idx].pred)