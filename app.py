from tkinter import *
import requests
from PIL import ImageTk, Image
from io import BytesIO


r = Tk() 
# r.wm_attributes('-alpha', 0.7)  

r.resizable(False, False) #disable resize
large_font = ('Verdana',30)

r.title('Weather App Python') 
# r.geometry("800x500")
# photo = PhotoImage(file = "bg.gif")

def weatherRender(data):
    var = StringVar()
    l1= Label( r, textvariable=var, font = "Verdana 35",width=100 ).place(relx=0.5,rely=0.3, anchor=CENTER)
    var.set(data)

def detailsRender(data):
    var = StringVar()
    label = Label( r, textvariable=var, font = "Verdana 18",width=100 ).place(relx=0.5,rely=0.37, anchor=CENTER)
    var.set(data)

def dayForcast(data,offset):
    l1= Label( r, text="7 Days Forecast", font = "Verdana 20 bold",width=24 ).place(relx=0.5,rely=0.495, anchor=CENTER)
    var = StringVar()
    label = Label( r, textvariable=var, font = "Verdana 18",width=30 ).place(relx=0.5,rely=(0.5+offset), anchor=CENTER)
    var.set(data)




def returnEntry(arg=None):
    # inputValue=textBox.get("1.0","end-1c")
    inputValue = myEntry.get()
    myEntry.delete(0, 'end')
    city = inputValue

    req = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=dd46a0e3651ca212ec10edbe60130d01")
    data= req.json()
    tempCurr = float(data['main']['temp']) - 273.15
    tempMax= float(data['main']['temp_max']) - 273.15
    tempMin= float(data['main']['temp_min']) - 273.15
    # print (req.json()['main']['temp_max'])

    weatherRender(str(round(tempCurr,2)) + "°C - "+ city.capitalize() +", "+ data['sys']['country'])
    detailsRender( str(data['weather'][0]['main']) + " | "+ "Humidity: " + str(data['main']['humidity']) + "% | Min: " + str(round(tempMin,2)) + "°C | Max:" + str(round(tempMax,2)) +"°C "  )

    req = requests.get("http://api.openweathermap.org/data/2.5/find?q="+city+"&units=metric&appid=dd46a0e3651ca212ec10edbe60130d01&cnt=7")
    data2= req.json()
    # print(data2)
    lis = data2['list']
    lis.pop(0) #pop today forcast
    offset = 0.05
    flag=2
    for x in lis:
        dayForcast(str(str(flag) +" Day - " + str(x["main"]["temp"]) + "°C  | " + x['weather'][0]['main'] ),offset)
        offset = offset + 0.05
        flag= flag+1
        # print (x["name"])

    # print (lis)

    print (tempCurr)


# frame=Frame(r, width=600, height=500, background="#475C7A")
# frame.pack()

# button = Button(r, text='Get Weather', width=25, command=r.destroy) 

FILENAME = 'img2.png'
canvas = Canvas(r, width=600, height=500)
canvas.pack()
tk_img = ImageTk.PhotoImage(file = FILENAME)
canvas.create_image(125, 125, image=tk_img)

myEntry = Entry(r,textvariable=1,width=20,font=large_font)


# myEntry.pack(ipady=3)

myEntry.focus()
myEntry.bind("<Return>",returnEntry)
myEntry.place(relx=0.5, rely=0.1, anchor=CENTER)
# myEntry.pack()


# textBox=Text(r, height=2, width=10)
# textBox.pack()
buttonCommit=Button(r, height=1, width=15, text="Get Weather", 
                    command=lambda: returnEntry(),highlightbackground='black').place(relx=0.5,rely=0.18, anchor=CENTER)

# buttonCommit.pack()
# button.pack()


var = StringVar()
label = Label( r, textvariable=var ).place(relx=0.5,rely=0.035, anchor=CENTER)
var.set("Enter City Below & Press Enter ")


imgURL = 'http://openweathermap.org/img/wn/10d@2x.png'
response = requests.get(imgURL)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
print (img)
# panel = Label(r, image=img ).place(relx=0.5,rely=0.3, anchor=CENTER)



r.mainloop() 
