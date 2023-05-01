import requests
import tkinter as tk

root= tk.Tk()

root.geometry('500x500')

def get_weather():
    api_key = 'your api key'
    location = entry.get()
    url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        result_label.config(text=(f'The weather in {location} is {weather} \nwith a temperature of {temperature} K, \nhumidity of {humidity}%, and wind speed of {wind_speed} m/s.'))
    else:
        result_label.config(text='Unable to get weather information.')

label= tk.Label(root, text='enter your location ')
#label.config(padx= 200, pady=400)

label.pack()

entry =tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get weather", command= get_weather)
button.pack()

result_label= tk.Label(root)
result_label.pack()

root.mainloop()
#if __name__ == '__main__':
    #root.mainloop()




