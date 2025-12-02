# Question 2: Print Whether File is Audio, Video, or Other
# Print the type of each file as Audio, Video, or Other.
# Audio: .mp3, .wav, .aac
# Video: .mp4, .avi, .mkv
# Example Input:
# files = ["song.mp3", "movie.mp4", "trailer.avi", "audio.wav", "readme.txt", "video.mkv", "clip.mp4"]
audio=[".mp3",".wav",".aac"]
video=[".mp4",".avi",".mkv"]
files=["song.mp3", "movie.mp4", "trailer.avi", "audio.wav", "readme.txt", "video.mkv", "clip.mp4"]
for i in range(len(files)):
    for j in audio:
        if j in files[i]:
            print(files[i],"-","audio")
    for k in video:
        if k in files[i]:
            print(files[i],"-","video")

