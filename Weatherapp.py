import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

def format_response(weather):
    try:
        name = weather["name"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]

        final_str = "City: %s \nConditions: %s \nTemperature (°C): %s" % (name, desc.capitalize(), temp)
    except:
        final_str = "There was a problem retrieving that information"

    return final_str

def get_weather(city):
    weather_key = "163046765f2837830ed3f197f2b6bc5d"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "metric"}
    response = requests.get(url, params=params)
    weather = response.json()

    label["text"] = format_response(weather)
#############################################################TKINTER BELOW
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="planetearth.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#404040", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=("Courier", 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=("Courier", 14), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg="#404040", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=("Courier", 18))
label.place(relwidth=1, relheight=1)

root.mainloop()