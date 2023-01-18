from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
from babel.dates import format_date, format_datetime, format_time
root = Tk()
root.title("Wheater App")
root.geometry("900x470+300+300")
root.configure(bg="#FFD700")
root.resizable(False, False)




def getWheater():
    city = textfield.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    timezone.config(text=result)
    long_lat.config(text=f"{round(location.latitude, 4)}°N,{round(location.longitude, 4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)


    # weather
    api = "https://api.openweathermap.org/data/3.0/onecall?lat=" + str(location.latitude) + "&lon=" + str(location.longitude) + "&units=metric&lang=ro&appid=5038b3a7eacaa86aabed29d1d4852698"
    json_data = requests.get(api).json()

    #print(json_data)

    # get data
    temp = json_data['current']['temp']
    humidity = json_data['current']['humidity']
    pressure = json_data['current']['pressure']
    wind = json_data['current']['wind_speed']
    description = json_data['current']['weather'][0]['description']

    #print(temp)
    #print(humidity)
    #print(pressure)
    #print(wind)
    #print(description)

    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=description)

    # cell1
    day1image = json_data['daily'][0]['weather'][0]['icon']

    photo1= ImageTk.PhotoImage(file=f"icon/{day1image}@2x.png")
    image1.config(image=photo1)
    image1.image=photo1

    tempday1= round(json_data['daily'][0]['temp']['day'],1)
    tempnight1 = round(json_data['daily'][0]['temp']['night'],1)
    day1temp.config(text=f"Day:{tempday1}°C\n Night:{tempnight1}°C")

    # cell2
    day2image = json_data['daily'][1]['weather'][0]['icon']

    img = (Image.open(f"icon/{day2image}@2x.png"))
    resized_image2=img.resize((50,50))
    photo2 = ImageTk.PhotoImage(resized_image2)
    image2.config(image=photo2)
    image2.image=photo2

    tempday2 = round(json_data['daily'][1]['temp']['day'],1)
    tempnight2 = round(json_data['daily'][1]['temp']['night'],1)
    day2temp.config(text=f"Day:{tempday2}°C\n Night:{tempnight2}°C")

    # cell3
    day3image = json_data['daily'][2]['weather'][0]['icon']

    img = (Image.open(f"icon/{day3image}@2x.png"))
    resized_image3 = img.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_image3)
    image3.config(image=photo3)
    image3.image = photo3

    tempday3 = round(json_data['daily'][2]['temp']['day'],1)
    tempnight3 = round(json_data['daily'][2]['temp']['night'],1)
    day3temp.config(text=f"Day:{tempday3}°C\n Night:{tempnight3}°C")

    # cell4
    day4image = json_data['daily'][3]['weather'][0]['icon']
    img = (Image.open(f"icon/{day4image}@2x.png"))
    resized_image4 = img.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_image4)
    image4.config(image=photo4)
    image4.image = photo4

    tempday4 = round(json_data['daily'][3]['temp']['day'],1)
    tempnight4 = round(json_data['daily'][3]['temp']['night'],1)
    day4temp.config(text=f"Day:{tempday4}°C\n Night:{tempnight4}°C")

    # cell5
    day5image = json_data['daily'][4]['weather'][0]['icon']
    img = (Image.open(f"icon/{day5image}@2x.png"))
    resized_image5 = img.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_image5)
    image5.config(image=photo5)
    image5.image = photo5

    tempday5 = round(json_data['daily'][4]['temp']['day'],1)
    tempnight5 = round(json_data['daily'][4]['temp']['night'],1)
    day5temp.config(text=f"Day:{tempday5}°C\n Night:{tempnight5}°C")

    # cell6
    day6image = json_data['daily'][5]['weather'][0]['icon']
    img = (Image.open(f"icon/{day6image}@2x.png"))
    resized_image6 = img.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_image6)
    image6.config(image=photo6)
    image6.image = photo6

    tempday6 = round(json_data['daily'][5]['temp']['day'],1)
    tempnight6 = round(json_data['daily'][5]['temp']['night'],1)
    day6temp.config(text=f"Day:{tempday6}°C\n Night:{tempnight6}°C")

    # cell7
    day7image = json_data['daily'][6]['weather'][0]['icon']
    img = (Image.open(f"icon/{day7image}@2x.png"))
    resized_image7 = img.resize((50, 50))
    photo7 = ImageTk.PhotoImage(resized_image7)
    image7.config(image=photo7)
    image7.image = photo7

    tempday7 = round(json_data['daily'][6]['temp']['day'],1)
    tempnight7 = round(json_data['daily'][6]['temp']['night'],1)
    day7temp.config(text=f"Day:{tempday7}°C\n Night:{tempnight7}°C")

    # days


    first = datetime.now()

    # result= format_date(first,"E", locale='ro')
    day1.config(text=first.strftime("%A"))
    second = first + timedelta(days=1)
    day2.config(text=second.strftime("%A"))
    third = first + timedelta(days=2)
    day3.config(text=third.strftime("%A"))
    forth = first + timedelta(days=3)
    day4.config(text=forth.strftime("%A"))
    fifth = first + timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))
    sixth = first + timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))
    seventh = first + timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))


##icon

image_icon = PhotoImage(file="Images/logo.png")
root.iconphoto(False, image_icon)

Round_box = PhotoImage(file="Images/Rounded Rectangle 1.png")
Label(root, image=Round_box, bg="#FFD700").place(x=45, y=110)

# label

label1 = Label(root, text="Temperatura", font=('Helvetica', 10), fg="white", bg="#203243")
label1.place(x=50, y=120)

label2 = Label(root, text="Umiditate", font=('Helvetica', 10), fg="white", bg="#203243")
label2.place(x=50, y=140)

label3 = Label(root, text="Presiune atm", font=('Helvetica', 10), fg="white", bg="#203243")
label3.place(x=50, y=160)

label4 = Label(root, text="Viteza vant", font=('Helvetica', 10), fg="white", bg="#203243")
label4.place(x=50, y=180)

label5 = Label(root, text="Descriere", font=('Helvetica', 10), fg="white", bg="#203243")
label5.place(x=50, y=200)

## searchbox

Search_image = PhotoImage(file="Images/Rounded Rectangle 3.png")
myimage = Label(image=Search_image, bg="#FFD700")
myimage.place(x=270, y=120)

weat_image = PhotoImage(file="Images/Layer 7.png")
wheaterimage = Label(root, image=weat_image, bg="#203243")
wheaterimage.place(x=290, y=127)

textfield = tk.Entry(root, justify='center', width=15, font=('poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
textfield.place(x=370, y=130)
textfield.focus()

Search_icon = PhotoImage(file="Images/Layer 6.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#203243", command=getWheater)
myimage_icon.place(x=645, y=125)

##Bottom box

frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

# bottom boxes

firstbox = PhotoImage(file="Images/Rounded Rectangle 2.png")
secondbox = PhotoImage(file="Images/Rounded Rectangle 2 copy.png")

Label(frame, image=firstbox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondbox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondbox, bg="#212120").place(x=800, y=30)

# clock ( we place time )

clock = Label(root, font=("Helvetica", 30, 'bold'), fg="white", bg="#FFD700")
clock.place(x=30, y=20)

# timezone

timezone = Label(root, font=("Helvetica", 20), fg="white", bg="#FFD700")
timezone.place(x=600, y=20)

long_lat = Label(root, font=("Helvetica", 10), fg="white", bg="#FFD700")
long_lat.place(x=600, y=50)

# thpwd

t = Label(root, font=("Helvetica", 8), fg="white", bg="#203243")
t.place(x=150, y=120)
h = Label(root, font=("Helvetica", 8), fg="white", bg="#203243")
h.place(x=150, y=140)
p = Label(root, font=("Helvetica", 8), fg="white", bg="#203243")
p.place(x=150, y=160)
w = Label(root, font=("Helvetica", 8), fg="white", bg="#203243")
w.place(x=150, y=180)
d = Label(root, font=("Helvetica", 8), fg="white", bg="#203243")
d.place(x=150, y=200)

# to continue
# 1 cell
frame1 = Frame(root, width=230, height=132, bg="#282829")
frame1.place(x=35, y=315)

day1 = Label(frame1, font="arial 15", bg="#282829", fg="#fff")
day1.place(x=100, y=5)

image1 = Label(frame1, bg="#282829")
image1.place(x=1, y=15)

day1temp=Label(frame1,bg="#282829",fg="#FFD700",font="arial 15 bold " )
day1temp.place(x=100,y=50)

# 2 cell
frame2 = Frame(root, width=70, height=115, bg="#282829")
frame2.place(x=305, y=325)

day2 = Label(frame2,bg="#282829", fg="#fff")
day2.place(x=10, y=2)

image2 = Label(frame2, bg="#282829")
image2.place(x=7, y=20)

day2temp=Label(frame2,bg="#282829",fg="#FFD700")
day2temp.place(x=1,y=70)

# 3 cell
frame3 = Frame(root, width=70, height=115, bg="#282829")
frame3.place(x=405, y=325)

day3 = Label(frame3,bg="#282829", fg="#fff")
day3.place(x=10, y=2)

image3 = Label(frame3, bg="#282829")
image3.place(x=7, y=20)


day3temp=Label(frame3,bg="#282829",fg="#FFD700")
day3temp.place(x=1,y=70)

# 4 cell
frame4 = Frame(root, width=70, height=115, bg="#282829")
frame4.place(x=505, y=325)

day4 = Label(frame4, bg="#282829", fg="#fff")
day4.place(x=10, y=2)

image4 = Label(frame4, bg="#282829")
image4.place(x=7, y=20)

day4temp=Label(frame4,bg="#282829",fg="#FFD700")
day4temp.place(x=1,y=70)

# 5 cell
frame5 = Frame(root, width=70, height=115, bg="#282829")
frame5.place(x=605, y=325)

day5 = Label(frame5,bg="#282829", fg="#fff")
day5.place(x=10, y=2)

image5 = Label(frame5, bg="#282829")
image5.place(x=7, y=20)

day5temp=Label(frame5,bg="#282829",fg="#FFD700")
day5temp.place(x=1,y=70)
# 6 cell
frame6 = Frame(root, width=70, height=115, bg="#282829")
frame6.place(x=705, y=325)

day6 = Label(frame6,bg="#282829", fg="#fff")
day6.place(x=10, y=2)

image6 = Label(frame6, bg="#282829")
image6.place(x=7, y=20)

day6temp=Label(frame6,bg="#282829",fg="#FFD700")
day6temp.place(x=1,y=70)
# 7 cell
frame7 = Frame(root, width=70, height=115, bg="#282829")
frame7.place(x=805, y=325)

day7 = Label(frame7,bg="#282829", fg="#fff")
day7.place(x=10, y=2)

image7 = Label(frame7, bg="#282829")
image7.place(x=7, y=20)

day7temp=Label(frame7,bg="#282829",fg="#FFD700")
day7temp.place(x=1,y=70)

root.mainloop()
