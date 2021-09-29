# import the liberary
from pytube import YouTube
# from pytube.cli import on_progress
from tqdm import tqdm
from colorama import Fore, init
init(autoreset=True)
def make_green(thing):
    return f'{Fore.GREEN + str(thing) + Fore.RESET}'

def inProgress():
    print(make_green("downloading"))

def finish():
    print(make_green("done"))
    # return make_green("done")

# get the link from user
link = input("enter link of video : ")

# https://youtu.be/7prJMz3pRaM


# create an object
video = YouTube(link)


for stream in video.streams.filter(progressive=True, res="720p"):
    print(stream)

print(f"title of this video : {video.title}")
print(f"length of this video : {video.length / 60} minutes")





# print(video.streams.get_highest_resolution())

finalVideo = video.streams.get_highest_resolution()
print(make_green("start downloading .."))
tqdm(finalVideo.download())

