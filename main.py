import os
from pytube import YouTube

if os.getcwd().split("//")[-1] != "youtube video downloader":
    os.chdir("youtube video downloader")

video_links = ["https://www.youtube.com/watch?v=eYVwF4OG-H4"]

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


for link in video_links:
    Download(link)