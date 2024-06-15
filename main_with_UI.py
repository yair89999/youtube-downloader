import tkinter as tk
from tkinter import ttk
from pytube import YouTube

root = tk.Tk()
root.title("YouTube Downloader")

# URL input
tk.Label(root, text="YouTube URL:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# File type selection
tk.Label(root, text="File Type:").grid(row=1, column=0, padx=10, pady=10)
file_type_var = tk.StringVar(value="mp4")
file_type_mp4 = tk.Radiobutton(root, text="MP4", variable=file_type_var, value="mp4")
file_type_mp3 = tk.Radiobutton(root, text="MP3", variable=file_type_var, value="mp3")
file_type_mp4.grid(row=1, column=1, sticky=tk.W, padx=10, pady=10)
file_type_mp3.grid(row=1, column=1, sticky=tk.E, padx=10, pady=10)

# Resolution selection
tk.Label(root, text="Resolution:").grid(row=2, column=0, padx=10, pady=10)
resolution_var = tk.StringVar(value="720p")
resolution_options = ["720p", "480p", "360p", "240p", "144p"]
resolution_menu = ttk.Combobox(root, textvariable=resolution_var, values=resolution_options)
resolution_menu.grid(row=2, column=1, padx=10, pady=10)

class VideoInformation:
    def __init__(self, link):
        self.video_link = link
        self.video_object = YouTube(link)

        self.video_information = {
            "channel_name": self.video_object.author,
            "channel_url": self.video_object.channel_url,
            "views": self.video_object.views,
            "length_sec": self.video_object.length,
            "length_min": str(int(self.video_object.length//60))+":"+str(self.video_object.length%60),
            "publish date": str(self.video_object.publish_date.day)+"/"+str(self.video_object.publish_date.month)+"/"+str(self.video_object.publish_date.year)
        }
        print(self.video_information)

global current_video_info
current_video_info = {}
def Download():
    global current_video_info
    link = url_entry.get()
    print(link)
    file_type = file_type_var.get().upper()
    resolution = resolution_var
    """
    file type = MP4, MP3
    resolution = 720p, 480p, 360p, 240p, 144p
    """
    youtubeObject = YouTube(link)

    current_video_info = VideoInformation(link=link, resolution=resolution)

    if file_type == "MP3": # download only the audio
        youtubeObject = youtubeObject.streams.get_audio_only()
    else: # download the video itself
        try: # try by the given resolution
            youtubeObject = youtubeObject.streams.get_by_resolution(resolution)
        except: # if had problem downloading it will download the highest resolution available
            youtubeObject = youtubeObject.streams.get_highest_resolution()
        
    try:
        youtubeObject.download()
    except Exception as e:
        print("An error was raised:",e)
        return
    print("Download is completed successfully")

def wrapper_func():
    Download()
    tk.Label(root, text="Video Information:").grid(row=4, column=0, padx=10, pady=10)
    tk.Label(root, text="Link: "+current_video_info.video_link).grid(row=5, column=0, padx=10, pady=10)
    tk.Label(root, text="Channel Name: "+current_video_info.video_information["channel_name"]).grid(row=6, column=0, padx=10, pady=10)
    tk.Label(root, text="Publish Date: "+current_video_info.video_information["publish date"]).grid(row=7, column=0, padx=10, pady=10)
    
    tk.Label(root, text="Views: "+str(current_video_info.video_information["views"])).grid(row=8, column=0, padx=10, pady=10)
    tk.Label(root, text="Video Length: "+current_video_info.video_information["length_min"]).grid(row=9, column=0, padx=10, pady=10)

# Download button
download_button = tk.Button(root, text="Download", command=wrapper_func)
download_button.grid(row=3, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
