from moviepy.editor import VideoFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import os
import video_download as downloader

def combine(video, audio, username):
    try:
        video_clip = VideoFileClip(video)
        audio_clip = AudioFileClip(audio)

        if audio_clip.duration > video_clip.duration:
            audio_clip = audio_clip.subclip(0, video_clip.duration)

        combined = video_clip.set_audio(audio_clip)

        file_path = os.path.dirname(video)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
            
        combined.write_videofile("result/"+username+".mp4", codec="libx264", audio_codec="aac", fps=24, verbose=False, logger=None, threads = 32)

    except Exception as e:
        print(f"Error: {e}")

def video_time(source_path):
    try:
        clip = VideoFileClip(source_path)
        response = int(clip.duration)
        return response

    except Exception as e:
        print(f"Error: {e}")
        
def video_crop(source_path, startAt, endAt, username):
    try:
        clip = VideoFileClip(source_path)
        
        cropped_clip = clip.subclip(startAt, endAt)
        
        cropped_clip.write_videofile(source_path, codec="libx264", audio_codec="aac")

        return source_path

    except Exception as e:
        print(f"Error: {e}")

