from pytube import YouTube
from datetime import datetime
def download_video(youtube_url, username, file_name):
    try:
        yt = YouTube(youtube_url)
        video = yt.streams.filter(file_extension='mp4', res='360p').first()
        download_folder = "source/"
        
        video.download(download_folder, filename= username+"_"+file_name+".mp4")

        return download_folder+"/"+username+"_"+file_name+".mp4"
        

    except Exception as e:
        print(f"Error: {e}")
