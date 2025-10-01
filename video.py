import yt_dlp
import os

# Ask for video URL
url = input("Enter video URL: ")

# Folder where videos will be saved
download_folder = "downloadedVideos"

# Make sure the folder exists
if not os.path.exists(download_folder):
    os.makedirs(download_folder)  # This will create it if it doesn't exist

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
    'progress_hooks': [lambda d: print(f"{d['_percent_str']} downloaded") if d['status'] == 'downloading' else None],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print(f"Video downloaded to '{download_folder}' folder.")
