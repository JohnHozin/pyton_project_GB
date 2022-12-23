import requests
city = input("Введите город: ")
r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=ea93f316cdc6510f861f965801f582d6&units=metric")
data = r.json()

print(data)
print(data['main']['temp'])
