from tkinter import *
from tkinter import *
from pygame import mixer
from tkinter import ttk
from PIL import Image, ImageTk
from time import strftime


def time_find():
    string_time=strftime('%H:%M:%S %p')
    status_bar1_time.config(text=string_time)
    status_bar1_time.after(1,time_find)
    
def song(event):
    text=event.widget.cget('text')
    mixer.init()
    music_play='Music Play <------------------------------------------>  '
    def song1():
        mixer.music.load(f"songs/{text}.mp3")
        mixer.music.play()
        status_bar.after(1,status)
        root.title(f"{text}   ----   Music Play")
    def status():
        var.set(f'{music_play}{text} ')
        status_bar.update()
    def repeat():
        pass
    if text=='1.song':
        song1()
        status()
    elif text=='2.song':
        status()
        song1()
    elif text=='3.song':
        status()
        song1()
    elif text=='4.song':
        status()
        song1()
    elif text=='5.song':
        status()
        song1()
    elif text=='6.song':
        status()
        song1()
    elif text=='7.song':
        song1()
        status()
    elif text=='8.song':
        status()
        song1()
    elif text=='9.song':
        status()
        song1()
    else:
        root.title('Music Stop .... ?')
        var.set('------------------------>  Music Stop  <------------------------')
        status_bar.update()
        mixer.music.stop()


root=Tk()
root.title('Song App -- By Haider Ali Jutt')

width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry(f"{width}x{height}")
root.configure(bg="black")


# scroll_bar=Scrollbar(root)
# scroll_bar.pack(side=RIGHT,fill=Y)

# text=Text(root,yscrollcommand=scroll_bar.set)
# text.pack()
# scroll_bar.config(command=text.yview)

# image=Image.open('songs/ph.jpg')
# image=image.resize((width,height),Image.ANTIALIAS)
# photo=ImageTk.PhotoImage(image)
# lbl1=Label(canvas,image=photo)
# lbl1.pack()








lbl=Label(root,text="Song App",font='Algerian 40 bold',bg='black',fg='gold')
lbl.pack()

list_of_song=['1.song','2.song','3.song','4.song','5.song','6.song','7.song','8.song','9.song']

var1=StringVar()
var1.set('radio')

for i in list_of_song:
    rad_btn=Radiobutton(root,text=i,value=i,variable=var1,bg='black',fg='gold',font='Courier 16 bold',relief=SUNKEN,borderwidth=3,padx=10,width=10)
    rad_btn.pack(side=TOP,fill=Y,pady=10,padx=100)
    rad_btn.bind('<Button-1>',song)




btn_stop=Button(root,text='Stop Music any way ..',width=20,bg='black',fg='green',borderwidth=2,relief=GROOVE,font='Algerian 12 normal')
btn_stop.pack(pady=10)
btn_stop.bind('<Button-1>',song)


frame=Frame(root,bg='black')
frame.pack(side=BOTTOM,fill=X)

var=StringVar()
var.set('-----------------------------------> Status Loading <------------------------------------')
status_bar=Label(frame,textvariable=var,bg='black',borderwidth=2,relief=SUNKEN,height=2,fg='green',font='Lucida 15 bold')
status_bar.pack(side=BOTTOM,fill=X)


status_bar1_time=Label(status_bar,bg='black',fg='green',font=('ds-digital',15))
status_bar1_time.pack(side='right')
time_find()



root.mainloop()

