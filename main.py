import video_crop as autobot
import video_download as downloader
import os

# command is {{username} {video_youtube_link} {audio_youtube_link} {sound_starting_time}}
command = input("Give me command: ")

audio = command.split(" ")[2]
username = command.split(" ")[0]
video = command.split(" ")[1]
startAt = int(command.split(" ")[3])

video_path = downloader.download_video(video, username, "video")
audio_path = downloader.download_video(audio, username, "audio")
video_duration = autobot.video_time(video_path)
cropped_name = audio_path.split(".")[0] + "_cropped.mp4"
cropped_source = autobot.video_crop(audio_path, startAt, startAt + video_duration, username)
autobot.combine(video_path, cropped_source, username)

if os.path.exists(video_path):
  os.remove(video_path)
if os.path.exists(audio_path):
  os.remove(audio_path)
