from tkinter import *
from tkinter import filedialog
from pytube import YouTube 
from tkinter import ttk

imageName = 'thumbnail.jpg'
root = Tk()
root.title("YouTube Downloader")
root.geometry("500x500")
#window.columnconfigure(0, weight = 1)
window0 = Frame(root)
window1 = Frame(root)
window2 = Frame(root)

def openLocate():
	global path
	path = filedialog.askdirectory()
	if len(path):
		pathLabel.config(text = path, fg = "green")

def getURL():
	global YT  
	global URL
	URL = enterBox.get()
	YT = YouTube(URL)
	downloadLabel.config(text = "OK checked", fg = "green")

def download():
	choice = ytdChoices.get()
	URL = enterBox.get()
	if URL != '':
		YT = YouTube(URL)
		if choice == 'Video':
			chosen = YT.streams.get_highest_resolution()
		else:
			chosen = YT.streams.filter(only_audio=True).first()
		chosen.download(path)
		downloadLabel.config(text = 'Downloaded')
	else:
		downloadLabel.config(text = 'Paste url again please!')

#enter video URL
enterLabel = Label(window0, text = "Enter the video URL: ", font = ("NexaBold", 15), fg = "green").pack(fill = X)
enterValue = StringVar()
enterBox = Entry(window0, width = 50, textvariable = enterValue)
enterBox.pack(side = LEFT)
getURLButton = Button(window0, bg = "orange", fg = "black", text = "getURL", command = getURL).pack(side = LEFT)

#choose save path
pathBrowseLabel = Label(window1, text = "Download to: ", font = ("NexaBold", 15), fg = "green").pack(side = LEFT)
pathBrowseButton = Button(window1, bg = "orange", fg = "black", text = "Browse", command = openLocate).pack(side = LEFT)

#path display
window2 = Frame(root)
pathLabel = Label(window2, text = "Choose directory please!", font = ("NexaLight", 11), fg = "red")
pathLabel.pack()

#Download Quality
ytdTypeLabel = Label(window2,text="Select quality",font=("NexaBold",15))
ytdTypeLabel.pack()

#combobox
choices = ["Video","Only Audio"]
ytdChoices = ttk.Combobox(window2,values=choices)
ytdChoices.pack()

#downloaded display
downloadLabel = Label(window2, text = "Not pasted URL yet", font = ("NexaBold", 15), fg = "red")
downloadLabel.pack()
downloadButton = Button(window2, width = 30, height = 2, bg = "orange", fg = "black", text = "Download", command = download)
downloadButton.pack()

window0.pack()
window1.pack()
window2.pack()

root.mainloop() 