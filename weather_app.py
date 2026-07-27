import tkinter as tk
from tkinter import TOP, ttk, messagebox, PhotoImage, Label, Button, Frame, BOTTOM
from timezonefinder import TimezoneFinder
from datetime import datetime, timedelta
import requests
import pytz
from PIL import Image, ImageTk
import random
import io

root = tk.Tk()
root.title("Weather App")
root.geometry("890x470+300+200")
root.configure(bg="#57adff")
root.resizable(False, False)


API_KEY = "19ff639b72a99de1f08d7b86c4f84af6"

def get_weather_icon(icon_code):
    """
    Download weather icon from OpenWeatherMap API
    """
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    response = requests.get(icon_url)
    img_data = response.content
    img = Image.open(io.BytesIO(img_data))
    img = img.resize((50, 50))
    return ImageTk.PhotoImage(img)

def simulate_weather(temp, humidity, wind_speed, description, icon):
    """
    Generate simulated weather data for the next days based on today's weather.
    """
    weather_data = []
    possible_icons = ['01d', '02d', '03d', '04d', '09d', '10d', '11d', '13d', '50d']
    
    for i in range(7):
       
        new_temp = temp + random.uniform(-3, 3)

       
        new_humidity = max(0, min(100, humidity + random.uniform(-5, 5)))
        new_wind_speed = max(0, wind_speed + random.uniform(-0.5, 0.5))

        
        new_icon = random.choice(possible_icons)

       
        weather_data.append((
            round(new_temp, 1),
            round(new_humidity),
            round(new_wind_speed, 1),
            description,
            new_icon
        ))

    return weather_data

def getWeather():
    city = textfield.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return

    try:
       
        weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(weather_url).json()

        if response.get("cod") != 200:
            messagebox.showerror("Error", response.get("message", "Invalid city!"))
            return

       
        temp = response["main"]["temp"]
        humidity = response["main"]["humidity"]
        pressure = response["main"]["pressure"]
        wind_speed = response["wind"]["speed"]
        description = response["weather"][0]["description"].capitalize()
        icon_code = response["weather"][0]["icon"]

      
        t.config(text=f"{temp}°C")
        h.config(text=f"{humidity}%")
        p.config(text=f"{pressure} hPa")
        w.config(text=f"{wind_speed} m/s")
        d.config(text=description)

       
        current_weather_icon = get_weather_icon(icon_code)
        weather_icon_label.config(image=current_weather_icon)
        weather_icon_label.image = current_weather_icon

      
        obj = TimezoneFinder()
        lat = response["coord"]["lat"]
        lon = response["coord"]["lon"]
        timezone_name = obj.timezone_at(lat=lat, lng=lon)
        timezone.config(text=timezone_name)

        home = pytz.timezone(timezone_name)
        local_time = datetime.now(home)
        clock.config(text=local_time.strftime("%I:%M %p"))

        
        today_day_label.config(text=f"Today: {local_time.strftime('%A')}")
         
        simulated_weather = simulate_weather(temp, humidity, wind_speed, description, icon_code)
        
       
        long_lat.config(text=f"{round(lat, 4)}°N, {round(lon, 4)}°E")

       
        for i, (frame, day_label, temp_label, img_label) in enumerate(forecast_frames):
            day_name = (local_time + timedelta(days=i)).strftime("%A")
            day_label.config(text=day_name)

          
            day_temp, day_humidity, day_wind_speed, day_description, day_icon = simulated_weather[i]
            temp_label.config(text=f"{day_temp}°C")

          
            icon_photo = get_weather_icon(day_icon)
            img_label.config(image=icon_photo)
            img_label.image = icon_photo

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")




image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)


Search_image = PhotoImage(file="Rounded Rectangle 3.png")
myimage = Label(image=Search_image, bg="#57adff")
myimage.place(x=270, y=120)



textfield = tk.Entry(root, justify="center", width=15, font=("poppins", 25, "bold"), bg="#203243", border=0, fg="white")
textfield.place(x=370, y=130)
textfield.focus()

Search_icon = PhotoImage(file="Layer 6.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWeather)
myimage_icon.place(x=645, y=125)


weather_icon_label = Label(root, bg="#203243")
weather_icon_label.place(x=290, y=127)

clock = Label(root, font=("Helvetica", 30, "bold"), fg="white", bg="#57adff")
clock.place(x=30, y=20)

today_day_label = Label(root, font=("Helvetica", 15), fg="white", bg="#57adff")
today_day_label.place(x=30, y=70)

timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#57adff")
timezone.place(x=700, y=20)

long_lat = Label(root, font=("Helvetica", 15), fg="white", bg="#57adff")
long_lat.place(x=700, y=60)

Round_box = PhotoImage(file="Rounded Rectangle 1.png")
Label(root, image=Round_box, bg="#57adff").place(x=30, y=110)


label1 = Label(root, text="Temperature", font=("Helvetica", 11), fg="white", bg="#203243")
label1.place(x=50, y=120)
t = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
t.place(x=150, y=120)

label2 = Label(root, text="Humidity", font=("Helvetica", 11), fg="white", bg="#203243")
label2.place(x=50, y=140)
h = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
h.place(x=150, y=140)

label3 = Label(root, text="Pressure", font=("Helvetica", 11), fg="white", bg="#203243")
label3.place(x=50, y=160)
p = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
p.place(x=150, y=160)

label4 = Label(root, text="Wind Speed", font=("Helvetica", 11), fg="white", bg="#203243")
label4.place(x=50, y=180)
w = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
w.place(x=150, y=180)

label5 = Label(root, text="Description", font=("Helvetica", 11), fg="white", bg="#203243")
label5.place(x=50, y=200)
d = Label(root, font=("Helvetica", 11), fg="white", bg="#203243")
d.place(x=150, y=200)


frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

forecast_frames = []
for i in range(7):
    x_offset = 35 + i * 120
    frame_box = Frame(root, width=90, height=130, bg="#282829")
    frame_box.place(x=x_offset, y=315)

    
    day_label = Label(frame_box, font=("Helvetica", 10), bg="#282829", fg="white")
    day_label.pack(side=TOP)

   
    img_label = Label(frame_box, bg="#282829")
    img_label.pack()


    temp_label = Label(frame_box, font=("Helvetica", 10), bg="#282829", fg="white")
    temp_label.pack()

    forecast_frames.append((frame_box, day_label, temp_label, img_label))

root.mainloop()
