# Weather App

 A simple Python-based GUI Weather App that shows the current weather conditions and a 7-day forecast for a given city. 
The app uses the OpenWeatherMap API to fetch weather data and is built using Tkinter for the user interface.

#Features  

	•	Displays current temperature, humidity, pressure, wind speed, and sky condition.
	•	Provides 7-day weather forecast.
	•	Allows searching for cities dynamically.
	•	Automatically shows local time and timezone of the city.
	•	Error handling for invalid or unrecognized city names.

# Requirements  

	•	Python 3.7 or higher
	•	Required Libraries:
	•	requests
	•	tkinter
	•	datetime
	•	Pillow (if using icons)

# Install dependencies:  
pip install requests Pillow

## How to Run  
	1.	Clone or download the repository.
	2.	Run the Python script:

python weather_app.py  

# Screenshots  

## Main Weather Interface:  
<img width="832" height="463" alt="Screenshot 2025-07-27 at 11 51 30 AM" src="https://github.com/user-attachments/assets/3fef4b97-242d-4eea-bb3f-bb0799c9309c" />

## Invalid City Error Handling:  
<img width="753" height="418" alt="Screenshot 2025-07-27 at 11 51 48 AM" src="https://github.com/user-attachments/assets/30ad0356-af80-4afc-b0ee-e40fbdb8d5ce" />

 ## Notes
	•	Make sure you have an active internet connection.
	•	To get accurate data, use correct city names or use the city ID (if modifying for that).

 ## File Structure  

weather_app/  
│
├── weather_app.py             # Main Python application file
├── README.md                  # Project overview and instructions
├── Screenshot...png           # Screenshots for UI and documentation


## Packaging as Executable (Windows)  

To convert this app to .exe:  
1.	Install PyInstaller:  
pip install pyinstaller

2.	Package the app:  
pyinstaller --onefile --windowed weather_app.py

3.	Find the .exe inside the dist/ folder.  
