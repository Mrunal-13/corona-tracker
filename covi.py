import tkinter as tk
import requests
import datetime
from tkinter import *
from tkinter.ttk import *
def getdata():
    api="https://disease.sh/v3/covid-19/all"
    data=requests.get(api).json()
    total_cases=str(data['cases'])
    total_deaths=str(data['deaths'])
    today_cases=str(data['todayCases'])
    today_deaths=str(data['todayDeaths'])
    today_recovered=str(data['todayRecovered'])
    updated_at=data['updated']
    date=datetime.datetime.fromtimestamp(updated_at/1e3)
    label.config(text="TOTAL CASES:-> "+total_cases+"\n"+"Total Deaths:->"+total_deaths
    +"\n"+"Today Cases:-> "+today_cases+"\n"+"Today deaths:-> "+today_deaths+"\n"+"Today Recoverd:->"
    +today_recovered)

    label2.config(text = date)


canvas=tk.Tk()
canvas.geometry("400x400")
canvas.title("covid 19 tracker")

f=("poppins",15,"bold")

button=tk.Button(canvas,font=f,text="fetch data",background = "light blue",command = getdata)
button.pack(pady=20)

label=tk.Label(canvas,font=f)
label.pack(pady=20)
label2=tk.Label(canvas,font=8)
label2.pack()
getdata()

canvas.mainloop()





