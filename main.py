import os
from pytube import YouTube

video_links = []

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
