import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city):
    api_key = "YOUR_API_KEY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data["cod"] != 200:
            raise Exception(data["message"])
        weather = {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }
        return weather
    except Exception as e:
        messagebox.showerror("Error", f"City not found: {e}")
        return None

def show_weather():
    city = city_entry.get()
    weather = get_weather(city)
    if weather:
        temperature_label.config(text=f"Temperature: {weather['temperature']} °C")
        humidity_label.config(text=f"Humidity: {weather['humidity']}%")
        pressure_label.config(text=f"Pressure: {weather['pressure']} hPa")
        wind_label.config(text=f"Wind Speed: {weather['wind_speed']} m/s")
        description_label.config(text=f"Description: {weather['description']}")

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")
root.resizable(False, False)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

search_button = tk.Button(root, text="Search", command=show_weather)
search_button.pack()

temperature_label = tk.Label(root, text="Temperature:", font=("Arial", 12))
temperature_label.pack()

humidity_label = tk.Label(root, text="Humidity:", font=("Arial", 12))
humidity_label.pack()

pressure_label = tk.Label(root, text="Pressure:", font=("Arial", 12))
pressure_label.pack()

wind_label = tk.Label(root, text="Wind Speed:", font=("Arial", 12))
wind_label.pack()

description_label = tk.Label(root, text="Description:", font=("Arial", 12))
description_label.pack()

root.mainloop()