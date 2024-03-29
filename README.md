# YouTube Video Downloader

This Python script allows users to download YouTube videos in 1080p resolution with sound. It provides a simple and user-friendly GUI built with Tkinter. The script uses the `pytube` library to download video and audio streams separately and then merges them into a single video with sound using FFmpeg.

## Summary

The YouTube Video Downloader is a Python script that lets users download YouTube videos with sound in 1080p resolution. The script comes with a user-friendly GUI made using Tkinter, making it easy to input the YouTube video link and select the download directory. It utilizes the `pytube` library to download video and audio streams separately and merges them into a single video with sound using FFmpeg. The merged video is stored in the specified directory, and the individual video and audio files are automatically deleted after the process is complete.

## Getting Started

1. Install the required libraries using the following command:
```
pip install pytube
```

2. Make sure you have `FFmpeg` installed on your system. If not, download it from the official website and add it to your system's PATH.

## Features

- Download YouTube videos with sound in 1080p resolution.
- User-friendly GUI to input the YouTube video link and select the download directory.
- Error handling for invalid links or download failures.

## How to Use

1. Run the script, and a GUI window will appear.
2. Enter the YouTube video link in the input field.
3. Click on the `Browse` button to select the download directory (optional).
4. Click the `Download` button to initiate the download process.

## Author

Vishhal Narkar 

## Data Storage

- The video and audio streams are temporarily stored in the specified download directory before merging.
- Once the video with sound is created, the individual video and audio files are deleted, leaving only the merged video in the directory.

## Note

- The script requires an `active internet connection` to download videos.
- Ensure that you have `permission to download` and use the videos in compliance with YouTube's terms of service.

## Disclaimer

This script is intended for `educational use only.` Downloading copyrighted materials from YouTube may violate their terms of service and may be illegal in some jurisdictions. The author is not responsible for any misuse of this script.

Enjoy downloading your favorite YouTube videos hassle-free with this handy Python script!
