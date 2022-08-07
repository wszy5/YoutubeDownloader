from tkinter import *
from turtle import width

window = Tk()
window.geometry("500x500")
window.title("Youtube downloader")
window.resizable(width=False, height=False)

url_label = Label(window, text="Podaj link do filmu na youtube").place(x=50,y=50)
yt_link = StringVar()
url = Entry(window, textvariable=yt_link, width=60).place(x=50, y=75)

format_label = Label(window, text="Wybierz format pliku").place(x=50, y=100)
format_file = StringVar()
r1 = Radiobutton(window, text='.mp3', value='mp3', variable=format_file).place(x=50, y=125)
r2 = Radiobutton(window, text='.mp4', value='mp4', variable=format_file).place(x=50, y=150)


def run():
    print(yt_link.get())
    print(format_file.get())


ok = Button(window,text="OK",command=run,justify="center",width=20,background='lightblue',fg='blue').place(x=85,y=175)

mainloop()