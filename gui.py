from tkinter import filedialog
from pytube import Playlist
from tkinter import *
from tkinter.ttk import Progressbar, Style
import threading
import webbrowser

def thread_func():
    thread_download=threading.Thread(target=lambda:fetch())
    thread_download.start()

def select():
    path=filedialog.askdirectory()
    choose_label.configure(text="Chosen Path : ")
    entry_2.insert(END,str(path))
    print(path)

def fetch():
    """ Pull All Youtube Videos from a Playlist """

    playlist = Playlist(str(link.get()))
    count=len(playlist.videos)
    i=1
    for links in playlist.videos:
        links.streams.get_highest_resolution().download(path.get(),filename=str(i)+" : "+str(links.title))
        print(str(i)+" : "+str(links.title))
        progress_percent=int((int(i)/int(count))*100)
        progress['value']=progress_percent
        video_label.config(text=str(links.title))
        progress_label.config(text=str(progress_percent)+" %")
        window.update_idletasks()
        i=i+1
    progress_percent=int(int(i)/int(count))*100
    progress['value']=progress_percent
        

window=Tk()
window.geometry("530x600")
window.title("Playlist Downloader")
window.resizable(False,False)

#logo
#logo=PhotoImage(file="download.png")
#window.iconphoto(False,logo)

Label(window,text="YouTube Playlist Downloader").pack(padx=5,pady=50)

link=StringVar()
path=StringVar()
percent=StringVar()

Label(window,text="Paste Link here : ").place(x=32,y=140)
entry=Entry(window,width=54,textvariable=link).place(x=140,y=140)


choose_label=Label(window,text="Choose Path : ")
choose_label.place(x=32,y=200)
entry_2=Entry(window,width=45,textvariable=path)
entry_2.place(x=140,y=200)
Button(window,text="Browse",command=select).place(x=418,y=196)


video_label=Label(window, font="arial 8")
video_label.place(x=13,y=280)

progress_label=Label(window, font="arial 12 bold")
progress_label.place(x=242,y=340)

S=Style()
S.configure("TProgressbar",foreground="green",background="white", thickness=40)
progress=Progressbar(window,length=495, orient=HORIZONTAL, mode="determinate")
progress['value']=0
progress.place(x=15,y=300)

Button(window,text="Download",command=thread_func).place(x=230,y=400)

new=1
url = "https://github.com/AbhishekTiwari-342123/youtube-playlist-downloader"

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(window, fg="blue",text = "View Developer",command=openweb)
Btn.place(x=215,y=470)

window.mainloop()
        
