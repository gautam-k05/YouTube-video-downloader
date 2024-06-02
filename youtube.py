# Import necessary modules from pytube and other libraries
from pytube import YouTube, Playlist, Search
from tabulate import tabulate
import sys
import tkinter as tk
from tkinter import filedialog

# Define the main function to handle user input and download choices
def main():
    root = tk.Tk()
    root.withdraw()
    print("\nWelcome to your youtube video downloader")
    print("What would you like to download(Choose one of the below)")

    # Define the menu content to be printed
    menu = [
        ["To Download", "Enter this"],
        ["One video with its URL", "1"],
        ["All videos from a playlist URL", "2"],
        ["Download video by search", "3"]
    ]

    # Print the menu using tabulate for better formatting
    print(tabulate(menu, headers="firstrow", tablefmt="grid"))
    # Take user input for the choice
    choise = input("Enter your choice (1,2,3): ").strip()

    # Connect the choices to the corresponding functions
    if choise == '1':
        url = input("Enter video URL: ")
        print(download_video(url))
    elif choise == '2':
        url = input("Enter Playlist URL: ")
        print(download_playlist(url))
    elif choise == '3':
        s = input("Enter your search: ")
        print(download_search(s))
    else:
        # Exit if the input is not valid
        sys.exit("Enter a valid choice")

def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")

    return folder


def get_media_type():
    media_type = input("Enter the media type to download (audio/video): ").lower().strip()
    if media_type not in ['audio', 'video']:
        print("Invalid media type. Please enter 'audio' or 'video'.")
        return get_media_type()
    return media_type

# Function to download a single video
def download_video(url):
    try:
        # Create YouTube object using the URL
        yt = YouTube(url)
        # Take user input for the media type
        media_type = get_media_type()
        stream = yt.streams.filter(only_audio=True).first() if media_type == 'audio' else yt.streams.filter(file_extension='mp4').get_highest_resolution()
        save_dir = open_file_dialog()
        print("Started download...")
        stream.download(output_path=save_dir)
        return f"'{stream.title}' by {yt.author} has downloaded successfully"
    except Exception as e:
        return f'Seems like the URL is incorrect, Check that this is a valid youtube video URL and Please try Again!'

# Function to download all videos from a playlist
def download_playlist(url):
    try:
        # Create Playlist object using the URL
        p = Playlist(url)
        # Take user input for the media type
        media_type = get_media_type()
        save_dir = open_file_dialog()
        playlist_path = save_dir + '/' + p.title
        print(f"Downloading Playlist: '{p.title}'")
        # Loop through each video in the playlist and download
        for yt in p.videos:
            stream = yt.streams.filter(only_audio=True).first() if media_type == 'audio' else yt.streams.filter(file_extension='mp4').get_highest_resolution()
            stream.download(output_path=playlist_path)
            print(f"'{yt.title}' has downloaded")
        return f"{len(p.video_urls)} videos downloaded from {p.title}"
    except Exception as e:
        return f'Seems like the URL is incorrect, Check that this is a valid youtube playlist URL and Please try Again!'

# Function to search and download a video
def download_search(search):
    try:
        # Create Search object with the query
        s = Search(search)
        # List search results
        for i, vid in enumerate(s.results):
            print(f"{i+1}- {vid.title}- {vid.author}")
        # Take user input for the index of the video to download
        yt_index = int(input("Enter the index of video you want to download: "))
        if 0 < yt_index < len(s.results):
            yt = s.results[yt_index-1]
            # Take user input for the media type
            media_type = get_media_type()
            save_dir = open_file_dialog()
            print(f"Downloading: {yt.title} by {yt.author}")
            # Select the stream based on media type
            stream = yt.streams.filter(only_audio=True).first() if media_type == 'audio' else yt.streams.filter(file_extension='mp4').get_highest_resolution()
            stream.download(output_path=save_dir)
            return f"Download complete: {yt.title}"
        else:
            return "Enter a Valid index from results"
    except Exception as e:
        print(f'An error occurred: {e}, please try again')

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
