# Header Files 
import os as os # Used to create directories, get current directories, deleate files
import subprocess # Used to use 'ffmeg' tool combining audio and video in one file 
from tkinter import * # GUI 
from tkinter import filedialog # Used to ask directory 
from tkinter import messagebox # Used to show error statement in a popup
from pytube import YouTube # Used to download Youtube Videos

directory = os.getcwd() #initiated directory to current working directory. 

# Functions Declared 
def getDirectory():     # Function to ask user the directory to download the file 
    global directory 
    directory = filedialog.askdirectory()
    if directory == None:
        directory = os.getcwd()

def getTitle():         # Algorithm to change the invalid charecters in Youtube Video Titles to vaild charecters
    title = videoTitle
    newTitle = ""
    for i in title:
        n = (ord(i))
        if(n >= 48 and n <= 57 or n >= 65 and n <= 90 or n >= 97 and n <= 122):
            newTitle = newTitle + i 
        else:
            newTitle = newTitle + "_"
    # newTitle = newTitle[0:len(newTitle)//2]
    return newTitle

def downloadVideo():    # Function that downloads videos, this function also calls combineFiles function
    try : 
        global directory
        yt = YouTube(userLink.get())
        print(yt.streams.filter(mime_type="audio/mp4"))
        video = yt.streams.get_by_itag(137)
        audio = yt.streams.get_by_itag(251)
        global videoTitle 
        videoTitle = video.title
        directory = directory + "/" + getTitle()
        os.mkdir(directory)
        directory_Video = directory + "/video.mp4"
        directory_Audio = directory + "/audio.webm"
        directory_Output = directory + "/" + getTitle() +".mp4"
        print(directory_Video,directory_Audio,directory_Output)
        # itag = 137 for 1080p videos (mp4)
        # itag = 251 for 160kbps audio (webm)
        video.download(output_path= directory, filename = "video.mp4")
        audio.download(output_path = directory,filename = "audio.webm")
        combineFiles(directory_Video,directory_Audio,directory_Output)
    except Exception as e:
        messagebox.showerror(title = "Error", message = "Error : "+str(e))
        print(str(e))

def combineFiles(mp4_file, webm_file, output_file):     # Function that combines the video and audio files
    try:
        subprocess.run(['ffmpeg', '-i', mp4_file, '-i', webm_file, '-c:v', 'copy', output_file], check=True)
        # ffmpeg -i video.mp4 -i audio.webm -c:v copy output.mp4
        os.remove(mp4_file)
        os.remove(webm_file)
    except Exception as e:
        messagebox.showerror(title = "Error", message = "Error : "+str(e))

# GUI 

root = Tk(className= " Youtube Video Downloader")
root.geometry("500x300")
Label(root,text = "Youtube Video Downloader",font=("Poppins bold",20),foreground = "red").pack()
Label(root,text = "Enter your Link here : ", font = "poppins").place(x = 10,y = 75,anchor = NW)
userLink = StringVar()
Entry(root,textvariable = userLink, font=("poopins",10)).place(x = 180,y = 81,anchor = NW, width = 285)
Label(root,text = "Select path : ", font = "poppins").place(x = 10,y = 110,anchor = NW)
Button(root,text = "Browse", command = getDirectory).place(x = 140,y = 110,anchor = NW,)
Button(root,text="Download",command = downloadVideo, bg = "red").pack(side = BOTTOM,pady = 50)
mainloop()