import glob
import subprocess
for filename in glob.iglob('*.mp4'):
     video= filename
     audio= video[:-3] + "m4a"
     print(audio)   
     subprocess.call(["ffmpeg", "-i", video ,"-i",audio, "-c", "copy", "out.mp4"], stdout=subprocess.PIPE)   
