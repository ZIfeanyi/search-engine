print("Credit to https://studygyaan.com/ for original idea")
import requests,webbrowser
from bs4 import BeautifulSoup
from tkinter import *
struct=Tk()
struct.geometry("354x350")
struct.title("My Search Engine: IF-TECH")
label=Label(struct,text="Personal Search Engine",bg="teal",fg="white",font=("Times",20,"bold"))
label.pack(side=TOP)
struct.config(background="teal")
text=StringVar()
def search():
     data=requests.get('https://www.google.com/search?q='+text.get())
     soup=BeautifulSoup(data.content,"html.parser")
     result=soup.select(".kCrYT a")
     for link in result[:5]:
         searching=link.get("href")
         searching=searching[7:]
         searching=searching.split("&")
         webbrowser.open(searching[0])
label=Label(struct,text="Enter here to search",bg="teal",fg="white",font=("Times",15,"bold"))
label.place(x=50,y=100)
enter=Entry(struct,font=("Times",10,"bold"),textvar=text,width=30,bd=2,bg="white")
enter.place(x=50,y=130)
button=Button(struct,text="Search",font=("Times",10,"bold"),width=30,bd=2,command=search)
button.place(x=50,y=170)
struct.print("Credit to https://studygyaan.com/ for original idea")
