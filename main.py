import os
import subprocess
from tkinter import *
from tkinter import filedialog
from pytube import YouTube

root = Tk(className= " Youtube Video Downloader")

directory = os.getcwd()

def createFolder():
    global directory
    directory = directory + "/" + getTitle()
    os.mkdir(directory)

def getDirectory():
    global directory 
    directory = filedialog.askdirectory()
    if directory == None:
        directory = os.getcwd()

def getTitle():
    title = videoTitle
    newTitle = ""
    for i in title:
        n = (ord(i))
        if(n >= 48 and n <= 57 or n >= 65 and n <= 90 or n >= 97 and n <= 122):
            newTitle = newTitle + i 
        else:
            newTitle = newTitle + "_"
    return newTitle

def downloadVideo():
    try : 
        createFolder()
        yt = YouTube(userLink.get())
        print(yt.streams.filter(mime_type="audio/mp4"))
        video = yt.streams.get_by_itag(137)
        audio = yt.streams.get_by_itag(251)
        global videoTitle 
        videoTitle = video.title
        directory_Video = directory + "/video.mp4"
        directory_Audio = directory + "/audio.webm"
        directory_Output = directory + "/" + getTitle() +".mp4"
        print(directory_Video,directory_Audio,directory_Output)
        # itag = 137 for 1080p videos 
        # itag = 251 for 160kbps audio
        video.download(output_path= directory, filename = "video.mp4")
        audio.download(output_path = directory,filename = "audio.webm")
        combineFiles(directory_Video,directory_Audio,directory_Output)
    except Exception as e:
        top = Toplevel(root)
        Label(top,text = "Error : "+str(e),font=('poopins',20)).pack()

def combineFiles(mp4_file, webm_file, output_file):
    try:
        subprocess.run(['ffmpeg', '-i', mp4_file, '-i', webm_file, '-c:v', 'copy', output_file], check=True)
        # ffmpeg -i video.mp4 -i audio.webm -c:v copy video480p.mp4
        os.remove(mp4_file)
        os.remove(webm_file)
        os.system('cls')
    # except subprocess.CalledProcessError as e:
    except Exception as e:
        top = Toplevel(root)
        Label(top,text = "Error : "+str(e),font=('poopins',20)).pack()

root.geometry("700x500")
Label(root,text = "Youtube Video Downloader", font=("Poppins bold",20)).pack()
Label(root,text = "Enter your Link here : ", font = "poppins").place(x = 10,y = 75,anchor = NW)
userLink = StringVar()
root.update()
Entry(root,textvariable = userLink, font=('poopins',10)).place(x = 180,y = 81,anchor = NW, width = (root.winfo_width()-215))
Label(root,text = "Select path : ", font = "poppins").place(x = 10,y = 110,anchor = NW)
Button(text = "Browse", command = getDirectory).place(x = 140,y = 110,anchor = NW,)
Button(root,text="Submit",command = downloadVideo).pack(side = BOTTOM,expand = True)
# Button(root,text="Submit",command = combineFiles).pack(side = BOTTOM,expand = True)

mainloop()


































































# # # Git Flow Code

# import os
# from moviepy.editor import *
# from tkinter import * 
# from tkinter import ttk,messagebox
# from slugify import slugify
# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# from pytube import YouTube
# from pytube import*
# import moviepy
# import moviepy.editor as mymovie

# Foldername =""
# videofolder=""
# audiofolder="" 
# def openloc():
#     global Foldername
#     Foldername=filedialog.askdirectory()
    
#     if(len(Foldername)>1):
#         locationnerror.config(text=Foldername,fg="green")
    
    
  
#     else:
#         locationnerror.config(text="Choose Directory",fg="red")
    
    
# def audioandvideocombine():
#     url=ytdentry.get()
#     yt = YouTube(url)
    
   
  
  
# def Download_vid():
#     choice = ytdchoices.get()
#     url=ytdentry.get()

    

#     if(len(url)>1):
#         ytderror.config(text="")
#         yt = YouTube(url)
        
        
    
  
#     if(choice == choices[0]):
#         filenamee=slugify(YouTube(url).title)
#         video=yt.streams.filter(adaptive=True).first()
#         size = yt.streams.filter(adaptive=True).first().filesize
        
#         try:
#             get=messagebox.askyesno("Do You Want To Download",f"File Size: {round(size* 0.000001, 2)} MB")
            
#             if get==True:
#                 video.download(Foldername,filenamee+".mp4")    
                
                 
#         except Exception as e:
#              messagebox.showerror("Check Your Internet Connection!")
        
        
    
    
#     elif(choice==choices[1]):
#        filenamee=slugify(YouTube(url).title)
#        audio = yt.streams.filter(only_audio=True).last().download(Foldername,filenamee+".webm")
       
#        clip = moviepy.editor.AudioFileClip(Foldername+"/"+filenamee+".webm")
       
#        clip.write_audiofile(Foldername+"/"+filenamee+".mp3")
#        clip.close()
#        os.remove(audio)
       
        
        
        
#     elif(choice==choices[2]):
        
#             filenamee=slugify(YouTube(url).title)
#             videofolder=(Foldername+ "/" + filenamee+".mp4")
#             audiofolder=(Foldername+ "/" + filenamee+".mp3")
        
            
#             inputvideo=videofolder
#             inputaudio=audiofolder
#             outputvideo=(Foldername+"/"+ filenamee+"last"+".mp4")
        
#             videoclip=mymovie.VideoFileClip(inputvideo)
#             audioclip=mymovie.AudioFileClip(inputaudio)
#             finalclip=videoclip.set_audio(audioclip)
#             finalclip.write_videofile(outputvideo,fps=60)
            
#             os.remove(videofolder)
#             os.remove(audiofolder)
            
        
  
        
        
#     else:
#         ytderror.config(text="Paste the link again",fg="red")
    
    
    
 

#     ytderror.config(text="Download Completed",fg="green")



# root = Tk()
# root.title("Youtube Video and Sound Converter")

# root.geometry("350x400")
# root.columnconfigure(0,weight=1)



# ytdlabel= Label(root,text="Enter URL:",font=("bahnschrift semilight",15))
# ytdlabel.grid()

# ytdentryvar=StringVar()
# ytdentry=Entry(root,width=50,textvariable=ytdentryvar)
# ytdentry.grid()

# ytderror=Label(root,text="Error",fg="red",font=("bahnschrift semilight",13))
# ytderror.grid()

# savelabel=Label(root,text="Save the Video",font=("bahnschrift semilight",15))
# savelabel.grid()

# saveEntry=Button(root,width=13,bg="red",fg="white",text="Choose Directory:",command=openloc)
# saveEntry.grid()

# locationnerror=Label(root,text="Directory causes Error",fg="red",font=("bahnschrift semilight",13))
# locationnerror.grid()





# choices = ["1080p","Audio","Combine"]
# ytdchoices = ttk.Combobox(root,values=choices)
# ytdchoices.grid()

    

# downloadbtn=Button(root,width=10,text="Apply",bg ="green",fg="lightyellow",font=("bahnschrift semilight",15),command=Download_vid)

# downloadbtn.grid()

# root.mainloop()
