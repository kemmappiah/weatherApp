from tkinter import *
import requests

window = Tk()
window.title("EMMAPP WEATHER APP")
window.geometry("500x500")
window.resizable(width=False, height=False)

location = StringVar()

location_label = Label(window, text="Enter Location")
location_label.place(x=30, y=100)
location_entry = Entry(window, textvariable=location)
location_entry.place(x=150, y=100)

cloud_pct_lbl = Label(window, text="Cloud Precipitation:")
cloud_pct_lbl.place(x=30, y=150)
cloud_pct = Label(window)
cloud_pct.place(x=200, y=150)
temp_lbl = Label(window, text="Ambient Temperature:")
temp_lbl.place(x=30, y=200)
temp = Label(window)
temp.place(x=200, y=200)
humidity_lbl = Label(window, text="Humidity:")
humidity_lbl.place(x=30, y=250)
humidity = Label(window)
humidity.place(x=200, y=250)
min_temp_lbl = Label(window, text="Minimum Temperature:")
min_temp_lbl.place(x=30, y=300)
min_temp = Label(window)
min_temp.place(x=200, y=300)
max_temp_lbl = Label(window, text="Maximum Temperature:")
max_temp_lbl.place(x=30, y=350)
max_temp = Label(window)
max_temp.place(x=200, y=350)
wind_speed_lbl = Label(window, text="Wind Speed:")
wind_speed_lbl.place(x=30, y=400)
wind_speed = Label(window)
wind_speed.place(x=200, y=400)
server_status_lbl = Label(window, width=50)
server_status_lbl.place(x=30, y=450)


def the_function():
    city = location_entry.get()
    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': 'smCEorEsKDv8R9P/E0k5hg==h3i3S0pSg94C65RK'})
    if response.status_code == requests.codes.ok:
        a = response.text
        b = a.split(",")
        cloud = b[0]
        cloud_split = cloud.split(":")
        cloud_pct.config(text=cloud_split[1] + "%")
        temperature = b[1]
        temperature_split = temperature.split(":")
        temp.config(text=temperature_split[1] + '\u00b0' + "C")
        actual_humidity = b[3]
        actual_humidity_split = actual_humidity.split(":")
        humidity.config(text=actual_humidity_split[1] + "%")
        min_temperature = b[4]
        min_temperature_split = min_temperature.split(":")
        min_temp.config(text=min_temperature_split[1] + '\u00b0' + "C")
        max_temperature = b[5]
        max_temperature_split = max_temperature.split(":")
        max_temp.config(text=max_temperature_split[1] + '\u00b0' + "C")
        the_wind_speed = b[6]
        the_wind_speed_split = the_wind_speed.split(":")
        wind_speed.config(text=the_wind_speed_split[1] + "m/s")
        server_status_lbl.config(text="Success😊", font=("Cambria", 12, "italic"), fg="green")
    else:
        print("Error:", response.status_code, response.text)
        server_status_lbl.config(text="😒Error:" + str(response.status_code) + response.text,
                                 font=("Cambria", 12, "bold"), fg="red")


enter_btn = Button(window, text="Enter", command=the_function)
enter_btn.place(x=300, y=100)

window.mainloop()
