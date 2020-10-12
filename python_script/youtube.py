import youtube_dl
import subprocess


def youtube_to_mp3(link):
    #ask the user for the video they want to download
    #video_url = input("Please enter the Youtube Video URL: ")

    # download and convert to mp3 and store in downloads folder
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=link, download=False
    )
    #title = video_info['title']
    #audio = f"../songs/mp3/{video_info['title']}.mp3"
    title = video_info['title'].replace(" ","_")
    audio = f"../songs/mp3/{title}.mp3"

    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': audio,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192', 
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    return title

    # Open the file once it has been downloaded
    # subprocess.call(["open", filename])

# download a file with only audio, to save space
# if the final goal is to convert to mp3
# if __name__ == '__main__':
#     youtube_to_mp3(link)