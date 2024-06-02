# YouTube-video-downloader
 A Python script for downloading YouTube videos and playlists. Supports both audio and video formats with a simple command-line interface.
 
#### Description:
This python based programme uses libraries like pytube, tabulate, sys, tkinter. Its main purpose is to download videos that have been posted on youtube offline to your device, This programme can do it in three ways:

1. Ask the user to put in the URL of the video and download it wherever the user wants it to, in their computer.
2. Ask for the url of a playlist that's available on youtube and saves the video wherever the user likes.
3. It can search youtube from your search command to get top results and download them

##### Functions:
This programme consists of mainly six functions, that are:

- `main`: The main function welcomes the user and gives them information about the programme. It gives them options in a tabular form Using the `tabulate` library, that they can choose from and redirects the programme using `conditionals` to the correct function according to the user's input.

- `open_file_dialog`: This function uses the `tkinter` Library to present the user with a dialogue box where they can select the path or position at which they want to save their downloaded video. This returns a string of the path that the user has selected.

- `get_media_type`: This function asks the user for the type of media in which they want to download their video, It provides them with the option of audio or video. Using conditionals, it makes sure that the result the user has entered satisfies the condition. And if it doesn't, it `recursively` calls itself until the condition is fulfilled. It returns the strength of the option entered by the user.

- `download_video`: This function is used when the user chooses the option to download a single video using its url. It takes in one argument which is the URL itself, The URL it takes is in the string format. It uses the `pytube` library to make an `Object` of the `YouTube class` from the url. Than some functions are applied on this class to get either the audio or the video version of the youtube object, And then using the download function of the youtube class The video is downloaded.

- `download_playlist`: This function is used when the user chooses the option to download a full playlist with the url. It takes in one argument which is the URL itself in the string format. The url is then passed through the `Playlist` Function of the `pytube` library. This function converts the url into an object of the playlist class that lies inside the library. Then we `iterate` over the list of videos in the playlist Which we get by using `.videos` On the playlist class. Then we get the objects of the youtube class inside the iteration and download the correct file based on the users choice of audio or video.

- `download_search`: This function searches on Youtube, Using the query given by the user, Using the `Search` function inside of the `pytube` library. It Gets the top results and prints The title of the videos out for the user to choose between. Then it asks the user which video they want to download based on the index of the video. It selects the video, according to the index given by the user and filtres it with the media given by the user. Then it downloads the video and stores it on the correct path using the `open_file_dialogue` box function.

Each function has its own error checking mechanism using `try and except` keywords, with a correct error message That tells the user what they should do next.

##### Useage

First, we will be presented with the welcome screen and the dialogue box in which we need to choose the options from:

```
Welcome to your youtube video downloader
What would you like to download(Choose one of the below)
+--------------------------------+--------------+
| To Download                    |   Enter this |
+================================+==============+
| One video with its URL         |            1 |
+--------------------------------+--------------+
| All videos from a playlist URL |            2 |
+--------------------------------+--------------+
| Download video by search       |            3 |
+--------------------------------+--------------+
Enter your choice (1,2,3):
```

So after the user enters their choice: 1,2,3. They're prompted to enter the url or their search query:

```
Enter video URL:
```

If a valid url is entered it goes ahead and asks which format you want to download your file in:
```
Enter the media type to download (audio/video):
```

After this, a dialogue box appears that asks the user to choose where they would want to store the file when it's downloaded. After that, the file is downloaded in the given folder Text appears confirming the download.

