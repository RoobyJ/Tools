from __future__ import unicode_literals
import yt_dlp as ytd

while True:
    data = [input('link: ')]
    if not data:
        continue
    ydl_opts = {
        'format': '22/best',
        'outtmpl': "C:/Users/rober/Downloads/music/%(title)s.mp4",
    }
    with ytd.YoutubeDL(ydl_opts) as ydl:
        ydl.download(data)
'''


df = pd.read_csv("jakis.csv")

for n in range(len(df['link'])):

    data = [df['link'][n]]

    ydl_opts = {
                'format': '22/best',
                'outtmpl': f"C:/Users/Black/Desktop/S05E{n+8}.mp4",
                #'postprocessors': [{
                    #'key': 'FFmpegExtractAudio',
                    #'preferredcodec': 'mp4',
                    #'preferredquality': '192',
                #}],
                }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(data)

'''
