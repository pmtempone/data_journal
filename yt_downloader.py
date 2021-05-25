import pytube

url = ['https://www.youtube.com/watch?v=dNi2hXZz5sg','https://www.youtube.com/watch?v=v0Saj7wSlZU','https://www.youtube.com/watch?v=018a1O7n-XI']

for i in url:
    print(i)
    youtube = pytube.YouTube(i)
    video = youtube.streams.first()
    video.download('/videos')