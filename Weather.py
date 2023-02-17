import tkinter as tk
import requests

def weather(core):
    location = text_string.get()
    api = "https://api.openweathermap.org" #Here insert your api key
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] -273.15)
    temp_min = int(json_data['main']['temp_min'] -273.15)
    temp_max = int(json_data['main']['temp_max'] -273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    final1 = f'Condition: {condition} {temp} °C'
    final2 = f'Temp min:{temp_min} °C Temp max:{temp_max} °C'
    final3 = f'Pressure: {pressure} Humidity: {humidity} Wind speed: {wind}'
    label1.config(text = final1)
    label2.config(text = final2)
    label3.config(text = final3)
    
    
core = tk.Tk()
core.title('MyWeatherApp')
core.geometry('600x500')
core.resizable(0, 0)

x = ('poppins', 15, 'bold')
y= ('poppins', 35, 'bold')

text_string = tk.Entry(core, bd = 3, justify = 'center', font = x)
text_string.pack(pady = 100)
text_string.focus()
text_string.bind('<Return>', weather)

label1 = tk.Label(core, font = y)
label1.pack()
label2 = tk.Label(core, font = x)
label2.pack()
label3 = tk.Label(core, font = x)
label3.pack()

core.mainloop()

