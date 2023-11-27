import subprocess
import os

for file in os.listdir():
    print(file)
    if os.path.isfile(file) and file[-4:] == ".wav":
        subprocess.call(['ffmpeg', '-i', f"{file}",
                         f"converted/{file[:-4]}.mp3"])
