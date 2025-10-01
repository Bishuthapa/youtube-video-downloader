# Video Downloader

A simple Python script to download videos from various platforms using yt-dlp.

## Features

- Download videos in the best available quality (video + audio)
- Automatic folder creation for downloaded content
- Real-time download progress display
- Support for multiple video platforms (YouTube, Vimeo, and more)

## Prerequisites

Before running this script, you need to have the following installed:

### 1. Python
- Python 3.7 or higher
- Download from [python.org](https://www.python.org/downloads/)

### 2. Required Python Package
- **yt-dlp**: A feature-rich command-line audio/video downloader

### 3. FFmpeg (Recommended)
- Required for merging video and audio streams
- Download from [ffmpeg.org](https://ffmpeg.org/download.html)

## Installation

### Step 1: Clone or Download the Script
```bash
git clone https://github.com/Bishuthapa/youtube-video-downloader.git
cd youtube-video-downloader
```

### Step 2: Install yt-dlp
```bash
pip install yt-dlp
```

### Step 3: Install FFmpeg

#### Windows:
1. Download FFmpeg from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract the files
3. Add the `bin` folder to your system PATH

#### macOS:
```bash
brew install ffmpeg
```

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install ffmpeg
```

## Usage

1. Run the script:
```bash
python video.py
```

2. When prompted, enter the video URL:
```
Enter video URL: https://www.youtube.com/watch?v=example
```

3. The video will be downloaded to the `downloadedVideos` folder in the same directory as the script.

## Download Location

All downloaded videos are saved in the `downloadedVideos` folder, which is automatically created in the script's directory if it doesn't exist.

## Supported Platforms

This script supports any platform that yt-dlp supports, including:
- YouTube
- Vimeo
- Facebook
- Twitter
- Instagram
- And many more

For a full list, visit the [yt-dlp supported sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

## Troubleshooting

### "No module named 'yt_dlp'"
- Make sure you've installed yt-dlp: `pip install yt-dlp`


#  How to Download Videos from Custom Sites with yt-dlp

This guide explains how to download videos from sites like `3-knot.vercel.app` using **yt-dlp** by finding the direct video link.

---

##  Step 1: Open Developer Tools

1. Open your video page in Chrome/Edge/Brave/Firefox.
2. Press **F12** (or `Ctrl + Shift + I`) to open Developer Tools.
3. Go to the **Network** tab.
4. Refresh the page (F5).

---

##  Step 2: Filter for Media Files

1. In Network, click the **Filter → Media** option.
2. Play the video. You should see requests like:

   * `.mp4`
   * `.webm`
   * `.m3u8` (streaming playlist)

Example request you might see:

```
https://3-knot.vercel.app/videos/abcd1234.mp4
```

---

## Step 3: Copy the Direct URL

1. Right-click the `.mp4` or `.m3u8` request.
2. Select **Copy → Copy link address**.

---

##  Step 4: Download with yt-dlp

Pass the copied link into your script:

```bash
python video.py
Enter video URL: https://3-knot.vercel.app/videos/abcd1234.mp4
```

* yt-dlp will download the video directly.

###  Notes:

* If the link is `.m3u8` (HLS stream), yt-dlp can download it but requires **FFmpeg**:

  ```bash
  ```

yt-dlp "[https://3-knot.vercel.app/stream/abcd1234/master.m3u8](https://3-knot.vercel.app/stream/abcd1234/master.m3u8)"

```
- DRM-protected videos **cannot be downloaded**.

---

Follow these steps to get the actual video URL and yt-dlp will handle the download automatically.
```


### Video and audio are in separate files
- Install FFmpeg to automatically merge video and audio streams

### Permission errors
- Run the script with appropriate permissions
- Ensure the directory is writable

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built with [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Inspired by the need for a simple video download solution
